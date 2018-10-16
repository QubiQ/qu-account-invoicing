# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    extra_cost = fields.Monetary(
        string=_('Extra cost'),
        currency_field='company_currency_id',
        copy=False,
        default=0.0
    )
    indirect_cost_line_ids = fields.Many2many(
        'indirect.cost.invoices',
        'invoice_line_ids',
        string=_('Indirect cost invoices'),
        copy=False,
    )
