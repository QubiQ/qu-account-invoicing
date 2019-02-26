# -*- coding: utf-8 -*-
# Copyright 2019 Valentin Vinagre Urteaga <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    # Load all unsold PO lines
    @api.onchange('purchase_id')
    def purchase_order_change(self):
        res = super(AccountInvoice, self).purchase_order_change()
        partner_id = self.partner_id.commercial_partner_id or \
            self.partner_id
        if partner_id.purchase_journal_id:
            self.journal_id = partner_id.purchase_journal_id.id
        return res

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        partner_id = self.partner_id.commercial_partner_id or \
            self.partner_id
        # Purchase
        if self.type in ('in_invoice', 'in_refund'):
            if partner_id.purchase_journal_id:
                self.journal_id = partner_id.purchase_journal_id.id
        # Sale
        else:
            if partner_id.sale_journal_id:
                self.journal_id = partner_id.sale_journal_id.id
        return res
