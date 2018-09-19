# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Custom fields
    invoice_type = fields.Selection(
        [('mail', _('Mail')),
         ('e_invoice', _('Electronic Invoice'))],
        string=_("Invoice Type"),
        default='mail'
    )
