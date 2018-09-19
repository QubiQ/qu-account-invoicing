# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    # Custom fields
    invoice_type = fields.Selection(
        [('mail', _('Mail')),
         ('e_invoice', _('Electronic Invoice'))],
        string=_("Invoice Type"),
    )

    """
    When changing the partner on an invoice, the account type
    is accordingly updated.
    """
    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        if self.partner_id:
            if self.partner_id.commercial_partner_id:
                self.invoice_type = self.partner_id.commercial_partner_id\
                 .invoice_type
            else:
                self.invoice_type = self.partner_id.invoice_type
        else:
            self.invoice_type = False
        return res

    """
    When creating a credit note from an invoice, the account type
    of the credit note will be the same as the invoice.
    """
    @api.model
    def _prepare_refund(self, invoice, date_invoice=None, date=None,
                        description=None, journal_id=None):
        values = super(AccountInvoice, self)._prepare_refund(invoice)
        values['invoice_type'] = invoice.invoice_type
        return values
