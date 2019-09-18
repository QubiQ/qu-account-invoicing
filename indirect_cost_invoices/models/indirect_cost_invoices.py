# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
import logging


class IndirectCostInvoices(models.Model):
    _name = "indirect.cost.invoices"
    _description = "Indirect cost invoices"

    name = fields.Char(
        string=_('Name'),
        copy=False,
        readonly=True,
        default=lambda self: _('New')
    )
    note = fields.Char(
        string=_('Note'),
        copy=False,
        help=_("Informative note.")
    )
    description = fields.Text(
        string=_('Description'),
        copy=False,
        help=_("Detailed description and notes.")
    )
    state = fields.Selection(
        [('draft', _('Draft')),
         ('done', _('Done')),
         ('cancel', _('Cancelled'))],
        string=_('Status'),
        required=True,
        readonly=True,
        copy=False,
        default='draft',
        help=_("When an indirect cost invoice is created, " +
               "the status is 'Draft'.\n" +
               "If the status changes to 'Done', the unit cost is calculated" +
               " and applied to the found invoice lines extra cost.\n" +
               "If the status changes to 'Cancelled', the changes made to the" +
               " invoice lines extra cost are undone.")
    )
    company_id = fields.Many2one(
        'res.company',
        readonly=True,
        default=lambda self: self.env.user.company_id
    )
    company_currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        currency_field='company_currency_id',
        string="Company Currency",
        readonly=True,
        store=True
    )
    amount_untaxed = fields.Monetary(
        related='invoice_id.amount_untaxed_signed',
        string=_('Untaxed Amount'),
        store=True,
        readonly=True,
        help=_("Purchase Invoice amount without taxes.")
    )
    unit_cost = fields.Float(
        string=_('Unit Cost'),
        store=True,
        readonly=True,
        copy=False,
        help=_("Average cost for each product unit in Sale Order Lines.")
    )
    invoice_id = fields.Many2one(
        'account.invoice',
        string=_('Invoice'),
        required=True,
        domain=[('indirect_cost_invoice_id', '=', False),
                ('type', '=', 'in_invoice'),
                ('state', 'in', ['open', 'paid'])],
        help=_("Purchase Invoice to use.")
    )
    partner_ids = fields.Many2many(
        'res.partner',
        string=_('Partners'),
        required=False,
        domain=[('customer', '=', True)]
    )
    product_ids = fields.Many2many(
        'product.product',
        string=_('Products'),
        required=False
    )
    category_ids = fields.Many2many(
        'product.category',
        string=_('Categories'),
        required=False
    )
    invoice_line_ids = fields.Many2many(
        'account.invoice.line',
        'indirect_cost_line_ids',
        string=_('Invoice Lines'),
        copy=False,
        readonly=True,
        required=False
    )
    type_search = fields.Selection(
        [('product', 'Product'),
         ('product_category', 'Product category')],
        string=_('Type search'),
        default='product',
        copy=False,
        required=True,
        help=_("Select if you want to filter invoice lines by:\n" +
               " - Products. \n" +
               " - Product Categories (only products in that category line).")
    )
    date_from = fields.Date(
        string=_('Date from'),
        required=True
    )
    date_to = fields.Date(
        string=_('Date to'),
        required=True
    )

    @api.multi
    @api.onchange('invoice_id')
    def depends_name(self):
        for sel in self:
            if sel.invoice_id:
                sel.name = sel.invoice_id.number

    @api.multi
    def action_invoice_draft(self):
        for sel in self:
            sel.write({
                'state': 'draft',
                'unit_cost': False,
                'invoice_line.ids': [(5, None, None)]
            })

    @api.multi
    def action_invoice_cancel(self):
        for sel in self:
            for invoice_line in sel.invoice_line_ids:
                invoice_line.extra_cost -= \
                   sel.unit_cost * invoice_line.quantity
            sel.invoice_id.indirect_cost_invoice_id = False
            sel.write({'state': 'cancel'})

    """
    Cálculo del Unit Cost y aplicación del Extra Cost a las Invoice Lines.
    """
    @api.multi
    def action_validate_ic_product(self):
        for sel in self:
            if sel.invoice_id.indirect_cost_invoice_id:
                raise ValidationError(_('This procedure has already been ' +
                                        'made for this purchase invoice!'))
            sel.invoice_id.indirect_cost_invoice_id = sel
            total_qty = 0.0
            invoice_ids = set()
            for partner_id in sel.partner_ids.ids:
                invoice_obj = self.env['account.invoice'].search([
                    ('partner_id', 'child_of', partner_id),
                    ('date', '>=', sel.date_from),
                    ('date', '<=', sel.date_to),
                    ('type', '=', 'out_invoice'),
                    ('state', 'in', ['open', 'paid']),
                    ('company_id', '=', sel.company_id.id)
                ])
                if invoice_obj:
                    for in_id in invoice_obj.ids:
                        invoice_ids.add(in_id)
            invoice_ids = list(invoice_ids)
            product_ids = set()
            if sel.type_search == 'product_category':
                for category_id in sel.category_ids:
                    product_id = self.env['product.product'].search([
                        ('categ_id', 'child_of', category_id.id)
                    ])
                    if product_id:
                        for pr_id in product_id.ids:
                            product_ids.add(pr_id)
                product_ids = list(product_ids)
                sel.product_ids = product_ids
            invoice_lines = self.env['account.invoice.line'].search([
                ('invoice_id', 'in', invoice_ids),
                ('product_id', 'in', sel.product_ids.mapped('id'))
            ])
            total_qty = sum(invoice_lines.mapped('quantity'))
            if total_qty == 0.0:
                raise ValidationError(_('The total quantity for the ' +
                                        'invoice lines is 0!'))
            unit_cost = sel.amount_untaxed/total_qty
            sel.unit_cost = unit_cost
            for invoice_line in invoice_lines:
                invoice_line.extra_cost += unit_cost * invoice_line.quantity
            sel.write({
                'invoice_line_ids': [(6, 0, invoice_lines.mapped('id'))],
                'state': 'done'
            })

    @api.multi
    def unlink(self):
        for invoice in self:
            if invoice.state not in ('draft', 'cancel'):
                raise UserError(_('You cannot delete an indirect cost ' +
                                  'invoice which is not in draft.'))
        return super(IndirectCostInvoices, self).unlink()
