# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        analytic_account_id = False
        if self.partner_id.analytic_account_sales:
            analytic_account_id = self.partner_id.analytic_account_sales
        self.analytic_account_id = analytic_account_id
        return super(SaleOrder, self).onchange_partner_id()
