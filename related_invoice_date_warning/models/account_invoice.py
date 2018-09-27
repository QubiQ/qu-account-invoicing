# -*- coding: utf-8 -*-
# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_open_date_warning(self):
        self.ensure_one()
        if self.type in ('out_invoice', 'out_refund'):
            if self.search_count([
                ('date_invoice', '>', self.date_invoice),
                ('company_id', '=', self.company_id.id),
                ('journal_id', '=', self.journal_id.id),
                ('type', '=', self.type),
                ('state', 'in', ['open', 'paid'])
            ]) > 0:
                view = self.env.ref('related_invoice_date_warning.' +
                                    'wizard_invoice_date_warning')
                return {
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.invoice',
                    'res_id': self.id,
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'view_mode': 'form',
                    'target': 'new',
                }
        self.action_invoice_open()
