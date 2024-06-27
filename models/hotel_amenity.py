from odoo import models, fields

class HotelAmenity(models.Model):
    _name = 'hotel.amenity'
    _description = 'Hotel Amenity'

    name = fields.Char('Amenity Name', required=True)
    description = fields.Text('Description')
