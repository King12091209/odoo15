from odoo import models, fields

class HotelBuilding(models.Model):
    _name = 'hotel.building'
    _description = 'Hotel Building'

    name = fields.Char(string='Building Name', required=True)
    address = fields.Char(string='Address')
    description = fields.Text(string='Description')
