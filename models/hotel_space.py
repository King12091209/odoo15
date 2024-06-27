from odoo import models, fields

class HotelSpace(models.Model):
    _name = 'hotel.space'
    _description = 'Hotel Space'

    name = fields.Char('Space Name', required=True)
    description = fields.Text('Description')
    capacity = fields.Integer('Capacity')
    status = fields.Selection([('available', 'Available'), ('occupied', 'Occupied')], default='available')
