# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountPaymentMode(models.Model):
    _inherit = 'account.payment.mode'

    not_check = fields.Boolean(
        string=_('Mail Notifications'),
        help=_("Set active to enable mail notifications each week.")
    )
