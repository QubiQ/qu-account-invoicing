# Copyright 2020 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def create(self, vals):
        res = super().create(vals)
        purchase_id = vals.get('purchase_id')
        if not purchase_id and vals.get('invoice_line_ids'):
            purchase_id = vals['invoice_line_ids'][0][2].get('purchase_id')
        if purchase_id:
            for attachment in self.env['ir.attachment'].search([
                ('res_model', '=', 'purchase.order'),
                ('res_id', '=', purchase_id)
            ]):
                attachment.copy({
                    'res_model': 'account.invoice', 'res_id': res.id
                })
        return res
