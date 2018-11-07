# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _get_payments(self):
        if self.move_id:
            return self.move_id.line_ids.filtered(
                lambda x: x.account_id == self.account_id
            )
