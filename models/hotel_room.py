from odoo import models, fields

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Name', required=True)
    building_id = fields.Many2one('hotel.building', string='Building', required=True)
    amenity_ids = fields.Many2many('hotel.amenity', string='Amenities')
    price = fields.Float(string='Price', required=True)
    standing = fields.Selection([('standard','Standard'), ('deluxe', 'Deluxe'), ('suite' , 'Suite')], default='standard')
 