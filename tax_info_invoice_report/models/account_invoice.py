# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    @api.depends(
        'invoice_line_ids.price_subtotal', 'tax_line_ids.amount',
        'tax_line_ids.amount_rounding', 'currency_id', 'company_id',
        'date_invoice', 'type'
    )
    def _compute_amount(self):
        if self.company_id.show_tax_info == 'yes' and\
            self.company_id.tax_ids and\
            len(set(self.company_id.tax_ids).intersection(
                self.invoice_line_ids.mapped('invoice_line_tax_ids')
            )) > 0 and self.company_id.info_text and\
            (not self.comment or
                self.comment.find(self.company_id.info_text) == -1):
            if not self.comment:
                self.comment = self.company_id.info_text
            else:
                self.comment += '\n' + self.company_id.info_text
        return super(AccountInvoice, self)._compute_amount()
