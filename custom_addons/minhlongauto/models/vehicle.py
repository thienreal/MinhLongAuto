from odoo import models, fields

class Vehicle(models.Model):
    _name = 'minhlongauto.vehicle'
    _description = 'Thông tin phương tiện'
    _rec_name = 'license_plate'

    name = fields.Char(string='Tên phương tiện', required=False)
    license_plate = fields.Char(string='Biển số xe', required=True)
    make = fields.Char(string='Hãng xe')
    model = fields.Char(string='Dòng xe')
    year = fields.Integer(string='Năm sản xuất')
    customer_id = fields.Many2one('res.partner', string='Khách hàng', domain=[('customer_rank', '>', 0)])
    vin = fields.Char(string='Số khung (VIN)')
    color = fields.Char(string='Màu sắc')
    mileage = fields.Float(string='Số km đã đi')
    notes = fields.Text(string='Ghi chú')