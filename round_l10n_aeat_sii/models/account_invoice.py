# Copyright 2019 Valentin Vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models, api


"""
Funcion recursiva para redondeo de floats en diccionarios i/o listas
de profundidad
"""


def floats_round_iterable(iterable, decimals=2):
    if type(iterable) == list:
        for x in range(len(iterable)):
            if type(iterable[x]) == dict:
                iterable[x] = floats_round_iterable(iterable[x])
            elif type(iterable[x]) == list:
                iterable[x] = floats_round_iterable(iterable[x])
            elif type(iterable[x]) == float:
                iterable[x] = round(iterable[x], decimals)
    if type(iterable) == dict:
        for x in iterable.keys():
            if type(iterable[x]) == dict:
                iterable[x] = floats_round_iterable(iterable[x])
            elif type(iterable[x]) == list:
                iterable[x] = floats_round_iterable(iterable[x])
            elif type(iterable[x]) == float:
                iterable[x] = round(iterable[x], decimals)
    return iterable


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _get_sii_out_taxes(self):
        res = super(AccountInvoice, self)._get_sii_out_taxes()
        res = floats_round_iterable(res)
        return res

    @api.multi
    def _get_sii_in_taxes(self):
        desglose_factura, tax_amount, not_in_amount_total =\
            super(AccountInvoice, self)._get_sii_in_taxes()
        desglose_factura = floats_round_iterable(desglose_factura)
        tax_amount = floats_round_iterable(tax_amount)
        not_in_amount_total = floats_round_iterable(not_in_amount_total)
        return desglose_factura, tax_amount, not_in_amount_total

    @api.multi
    def _get_sii_tax_dict(self, tax_line, sign):
        res = super(AccountInvoice, self)._get_sii_tax_dict(tax_line, sign)
        res = floats_round_iterable(res)
        return res
