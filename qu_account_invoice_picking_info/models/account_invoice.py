# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    picking_docs = fields.Char(string='Pickings', compute='_getPickingNames')

    @api.multi
    def _getPickingNames(self):
        for sel in self:
            sel.picking_docs = ', '.join(
                map(lambda x: (x.picking_id.name), sel.move_line_ids))
