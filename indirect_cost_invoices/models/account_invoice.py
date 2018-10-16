# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    indirect_cost_invoice_id = fields.Many2one(
        'indirect.cost.invoices',
        string=_('Indirect cost invoice'),
        copy=False,
        required=False,
    )
