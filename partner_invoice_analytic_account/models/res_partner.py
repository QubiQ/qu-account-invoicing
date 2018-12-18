# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    analytic_account_sales = fields.Many2one(
        comodel_name='account.analytic.account',
        string=_('Sales Analytic Account'),
        company_dependent=True
    )
    analytic_account_purchases = fields.Many2one(
        comodel_name='account.analytic.account',
        string=_('Purchases Analytic Account'),
        company_dependent=True
    )
