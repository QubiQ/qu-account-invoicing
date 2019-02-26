# -*- coding: utf-8 -*-
# Copyright 2019 Valentin Vinagre Urteaga <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ModelName(models.Model):
    _inherit = "res.partner"

    sale_journal_id = fields.Many2one(
        'account.journal',
        string=_('Sale Journal'),
        domain=[('type', '=', 'sale')],
        help=_('If set, this journal is chosen by default in sale invoices')
    )
    purchase_journal_id = fields.Many2one(
        'account.journal',
        string=_('Purchase Journal'),
        domain=[('type', '=', 'purchase')],
        help=_('If set, this journal is chosen by default in'
               ' purchase invoices')
    )
