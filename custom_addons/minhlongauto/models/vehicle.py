from odoo import models, fields

class Vehicle(models.Model):
    _name = 'minhlongauto.vehicle'
    _description = 'Vehicle Information'

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year')
    customer_id = fields.Many2one('res.partner', string='Customer', domain=[('customer_rank', '>', 0)])
    vin = fields.Char(string='VIN')
    color = fields.Char(string='Color')
    mileage = fields.Float(string='Mileage')
    notes = fields.Text(string='Notes')