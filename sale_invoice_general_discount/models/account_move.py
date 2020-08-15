# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    global_disc = fields.Float(string="General Discount (%)")
    global_disc_amount = fields.Float(string="General Imp. Discount",
                                      compute="_compute_global_disc")

    @api.depends('invoice_line_ids.global_disc_amount')
    def _compute_global_disc(self):
        self.global_disc_amount = sum(
            self.invoice_line_ids.mapped('global_disc_amount'))

    def _recompute_tax_lines(self, recompute_tax_base_amount=False):
        prices = {}
        for line in self.line_ids.filtered(
                lambda line: not line.tax_repartition_line_id):
            extra_discount = 1 - (line.global_disc / 100)
            prices[line.id] = line.price_unit
            line.price_unit = line.price_unit * extra_discount
        res = super()._recompute_tax_lines(recompute_tax_base_amount)
        for line in self.line_ids.filtered(
                lambda line: not line.tax_repartition_line_id):
            if prices.get(line.id):
                line.price_unit = prices[line.id]
        return res


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    global_disc = fields.Float(compute="_compute_global_disc",
                               store=True,
                               readonly=False)

    global_disc_amount = fields.Float(string="General Imp. Discount",
                                      compute="_compute_disc_amount")

    @api.depends('quantity', 'price_unit', 'discount', 'global_disc')
    def _compute_disc_amount(self):
        self.global_disc_amount = 0
        for rec in self.filtered('global_disc'):
            subtotal = rec.quantity * rec.price_unit
            if rec.discount:
                subtotal *= 1 - (rec.discount / 100)
            rec.global_disc_amount = (subtotal * rec.global_disc / 100)

    @api.depends('move_id.global_disc')
    def _compute_global_disc(self):
        self.global_disc = 0
        for rec in self.filtered(lambda x: x.product_id.type == "product"):
            rec.global_disc = rec.move_id.global_disc

    def _get_price_total_and_subtotal(self,
                                      price_unit=None,
                                      quantity=None,
                                      discount=None,
                                      currency=None,
                                      product=None,
                                      partner=None,
                                      taxes=None,
                                      move_type=None,
                                      global_disc=None):
        self.ensure_one()
        if self.product_id.type != "product":
            global_disc_2 = 0
        else:
            global_disc_2 = self.global_disc
        price_unit = price_unit or self.price_unit
        discount = discount or self.discount
        price_unit = price_unit * (1 - (discount/100))
        return self._get_price_total_and_subtotal_model(
            price_unit=price_unit,
            quantity=quantity or self.quantity,
            discount=global_disc or global_disc_2,
            currency=currency or self.currency_id,
            product=product or self.product_id,
            partner=partner or self.partner_id,
            taxes=taxes or self.tax_ids,
            move_type=move_type or self.move_id.type,
        )

    @api.onchange("quantity", "discount", "price_unit", "tax_ids",
                  "discount_fixed", "global_disc")
    def _onchange_price_subtotal(self):
        return super()._onchange_price_subtotal()

    def create(self, vals):
        res = super().create(vals)
        for rec in res.filtered('sale_line_ids'):
            rec.price_unit = sum(rec.sale_line_ids.mapped('price_unit'))
        return res
