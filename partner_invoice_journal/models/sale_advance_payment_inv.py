# -*- coding: utf-8 -*-
# Copyright 2019 Valentin Vinagre Urteaga <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def create_invoices(self):
        res = super(SaleAdvancePaymentInv, self).create_invoices()
        sale_orders = self.env['sale.order'].browse(
            self._context.get('active_ids', [])
        )
        for inv in sale_orders.mapped('invoice_ids').filtered(
                lambda x: x.state == 'draft'):
            partner_id = inv.partner_id.commercial_partner_id or inv.partner_id
            if partner_id.sale_journal_id:
                inv.journal_id = partner_id.sale_journal_id
        return res
