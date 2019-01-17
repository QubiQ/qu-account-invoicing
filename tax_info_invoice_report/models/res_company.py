# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    show_tax_info = fields.Selection([
        ('yes', _('Yes')),
        ('no', _('No'))],
        default='no',
        string=_('Show Tax Info'),
        help=_(
            'Select yes to show an information text about taxes on invoice '
            'reports'
        )
    )
    tax_ids = fields.Many2many(
        comodel_name='account.tax',
        string=_('Taxes'),
        help=_('Select the taxes for which the text will be displayed')
    )
    info_text = fields.Text(
        string=_('Information Text'),
        translate=True,
        help=_('This text will appear at the end of the invoice report')
    )
