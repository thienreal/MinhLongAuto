from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vehicle_id = fields.Many2one(
        'minhlongauto.vehicle',
        string='Phương tiện',
        help='Chọn xe của khách hàng (tùy chọn)'
    )

    # Computed fields for statistics
    product_count = fields.Integer(
        string='Số SP hàng hóa',
        compute='_compute_order_statistics',
        store=True
    )
    service_count = fields.Integer(
        string='Số SP dịch vụ',
        compute='_compute_order_statistics',
        store=True
    )
    combo_count = fields.Integer(
        string='Số SP combo',
        compute='_compute_order_statistics',
        store=True
    )
    product_total = fields.Monetary(
        string='Tổng tiền hàng hóa',
        compute='_compute_order_statistics',
        store=True
    )
    service_total = fields.Monetary(
        string='Tổng tiền dịch vụ',
        compute='_compute_order_statistics',
        store=True
    )
    combo_total = fields.Monetary(
        string='Tổng tiền combo',
        compute='_compute_order_statistics',
        store=True
    )

    @api.depends('order_line.product_id', 'order_line.price_subtotal')
    def _compute_order_statistics(self):
        for order in self:
            product_count = 0
            service_count = 0
            combo_count = 0
            product_total = 0.0
            service_total = 0.0
            combo_total = 0.0

            for line in order.order_line:
                if line.display_type:  # Skip section/note lines
                    continue
                
                product = line.product_id
                if not product:
                    continue

                # Classify by product type
                if product.type == 'service':
                    service_count += int(line.product_uom_qty)
                    service_total += line.price_subtotal
                elif product.type == 'combo':
                    combo_count += int(line.product_uom_qty)
                    combo_total += line.price_subtotal
                else:  # product, consu
                    product_count += int(line.product_uom_qty)
                    product_total += line.price_subtotal

            order.product_count = product_count
            order.service_count = service_count
            order.combo_count = combo_count
            order.product_total = product_total
            order.service_total = service_total
            order.combo_total = combo_total

    @api.onchange('partner_id')
    def _onchange_partner_id_vehicle(self):
        """When partner changes, clear vehicle_id if it doesn't belong to new partner"""
        if self.vehicle_id and self.vehicle_id.customer_id != self.partner_id:
            self.vehicle_id = False
