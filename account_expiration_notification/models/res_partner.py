# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields
from datetime import datetime


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def send_exp_not(self):
        for pay_mode in self.env['account.payment.mode'].search(
         [('not_check', '=', True)]):

            ctx = {}
            current_company_id = pay_mode.company_id
            ctx['company_id_ctx'] = current_company_id
            ctx['pay_mode_ctx'] = pay_mode.id
            current_date = fields.Date.today()
            next_date = fields.Date.to_string(
                fields.Date.from_string(current_date)
                + datetime.timedelta(days=7))

            for partner_id in self.env['account.move.line'].read_group(
                [('payment_mode_id', '=', pay_mode.id),
                 ('date_maturity', '>=', current_date),
                 ('date_maturity', '<=', next_date),
                 ('company_id', '=', current_company_id.id)],
                ['partner_id'],
                ['partner_id'],
                 ):

                try:
                    template = self.env.ref(
                        'account_expiration_notification.email_template_acc_not')
                except ValueError:
                    template = False

                partner = self.browse([partner_id['partner_id'][0]])[0]
                template.with_context(ctx=ctx).send_mail(partner.id)

    def get_account_data(self):
        records = []
        current_date = fields.Date.today()
        next_date = fields.Date.to_string(fields.Date.from_string(current_date)
                                          + datetime.timedelta(days=7))
        ctx = self.env.context['ctx']
        pay_mode = ctx['pay_mode_ctx']

        for move_line in self.env['account.move.line'].search(
            [('payment_mode_id', '=', pay_mode),
             ('partner_id', '=', self.id),
             ('date_maturity', '>=', current_date),
             ('date_maturity', '<=', next_date),
             ('debit', '>', 0.0)],
        ):
            account_move = {}
            account_move['invoice'] = move_line.invoice_id.number
            account_move['invoice_date'] = move_line.invoice_date
            account_move['date_maturity'] = move_line.date_maturity
            account_move['effect_type'] = " "
            account_move['debit'] = move_line.debit
            account_move['comment'] = move_line.name

            records.append(account_move)

        return records
