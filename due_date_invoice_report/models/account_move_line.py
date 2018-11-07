# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_payment = fields.Many2one(
        comodel_name='account.invoice',
        inverse_name='payments',
        string=_('Invoice Payment')
    )
