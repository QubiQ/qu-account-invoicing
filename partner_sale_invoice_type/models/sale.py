# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    """
    Collects invoice type from the partner and applies it to the
    created invoice.
    """
    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.partner_id:
            if self.partner_id.commercial_partner_id:
                invoice_vals['invoice_type'] = self.partner_id\
                 .commercial_partner_id.invoice_type
            else:
                invoice_vals['invoice_type'] = self.partner_id.invoice_type
        else:
            invoice_vals['invoice_type'] = False
        return invoice_vals
