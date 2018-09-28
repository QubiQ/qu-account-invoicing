# Copyright 2015-2017 Akretion (http://www.akretion.com)
# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    standard_price_company_currency = fields.Float(
        string='Cost Price in Company Currency', readonly=True,
        digits=dp.get_precision('Product Price'),
        compute='_calculate_cost',
        store=True,
        help="Cost price in company currency in the unit of measure "
        "of the invoice line (which may be different from the unit "
        "of measure of the product).")
    margin = fields.Monetary(
        string='Margin in Company Currency', readonly=True, store=True,
        compute='_compute_margin')
    margin_rate = fields.Float(
        string="Margin Rate", readonly=True, store=True,
        compute='_compute_margin',
        digits=(16, 2), help="Margin rate in percentage of the sale price")

    @api.depends('product_id', 'quantity')
    def _calculate_cost(self):
        for sel in self:
            quantity = sel.uom_id._compute_quantity(
                sel.quantity, sel.product_id.uom_id)
            sel.standard_price_company_currency = \
                sel._get_anglo_saxon_price_unit()*quantity

    @api.depends(
        'standard_price_company_currency', 'invoice_id.currency_id',
        'invoice_id.type', 'invoice_id.company_id',
        'invoice_id.date_invoice', 'quantity', 'price_subtotal')
    def _compute_margin(self):
        for l in self:
            inv = l.invoice_id
            if inv and inv.type in ('out_invoice', 'out_refund'):
                # Importe en moeneda de la compañía
                price = inv.company_id.currency_id.with_context(
                        date=inv.date_invoice).compute(
                            l.price_subtotal,
                            inv.company_currency_id)
                l.margin = price - l.standard_price_company_currency
                if price != 0:
                    l.margin_rate = l.margin / price


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    margin_company_currency = fields.Monetary(
        string='Margin in Company Currency',
        readonly=True, compute='_compute_margin_cost', store=True,
        )
    cost = fields.Monetary(
        string='Cost in Company Currency',
        readonly=True, compute='_compute_margin_cost', store=True,
        )
    margin_rate = fields.Float(
        string="Margin Rate", readonly=True, store=True,
        compute='_compute_margin_cost',
        digits=(16, 2), help="Margin rate in percentage of the sale price")

    @api.depends(
        'type',
        'invoice_line_ids.margin',
        'invoice_line_ids.standard_price_company_currency')
    def _compute_margin_cost(self):
        for inv in self:

            margin_comp_cur = 0.0
            cost = 0.0
            sale = 0.0
            if inv.type in ('out_invoice', 'out_refund'):
                for il in inv.invoice_line_ids:
                    margin_comp_cur += il.margin
                    cost += il.standard_price_company_currency
                    sale += inv.company_id.currency_id.with_context(
                        date=inv.date_invoice).compute(
                            il.price_subtotal,
                            inv.company_currency_id)
            inv.margin_company_currency = margin_comp_cur
            inv.cost = cost
            if sale != 0:
                inv.margin_rate = inv.margin_company_currency / sale
