# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    global_disc = fields.Float(string="General Discount (%)")
    global_disc_amount = fields.Float(
        string="General Dis. Amount", compute="_compute_global_disc")

    @api.depends('order_line.global_disc_amount')
    def _compute_global_disc(self):
        self.global_disc_amount = sum(self.order_line.mapped(
                'global_disc_amount'))

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res['global_disc'] = self.global_disc
        res['global_disc_amount'] = self.global_disc_amount
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    global_disc = fields.Float(related="order_id.global_disc")
    global_disc_amount = fields.Float(compute="_compute_amount")


    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id',
                 'global_disc')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            extra_discount = (1 - (line.global_disc or 0.0) / 100.0)
            price_wo_discount = line.price_unit * (
                1 - (line.discount or 0.0) / 100.0)
            price = price_wo_discount * extra_discount
            disc_amount = price_wo_discount - price
            taxes = line.tax_id.compute_all(
                price,
                line.order_id.currency_id,
                line.product_uom_qty,
                product=line.product_id,
                partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax':
                sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total':
                taxes['total_included'],
                'price_subtotal':
                taxes['total_excluded'],
                'global_disc_amount': disc_amount,
            })
            if self.env.context.get(
                    'import_file',
                    False) and not self.env.user.user_has_groups(
                        'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'],
                                             [line.tax_id.id])
