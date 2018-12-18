# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        account_analytic_id = False
        if self.type in ['out_invoice', 'out_refund'] and\
                self.partner_id.analytic_account_sales:
            account_analytic_id = self.partner_id.analytic_account_sales
        elif self.type in ['in_invoice', 'in_refund'] and\
                self.partner_id.analytic_account_purchases:
            account_analytic_id =\
                self.partner_id.analytic_account_purchases
        for line in self.invoice_line_ids:
            line.account_analytic_id = account_analytic_id
        return super(AccountInvoice, self)._onchange_partner_id()


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        account_analytic_id = False
        if self.invoice_type in ['out_invoice', 'out_refund'] and\
                self.partner_id.analytic_account_sales:
            account_analytic_id = self.partner_id.analytic_account_sales
        elif self.invoice_type in ['in_invoice', 'in_refund'] and\
                self.partner_id.analytic_account_purchases:
            account_analytic_id =\
                self.partner_id.analytic_account_purchases
        self.account_analytic_id = account_analytic_id
