from odoo import models, fields

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in = fields.Datetime(string='Check-In Date', required=True)
    check_out = fields.Datetime(string='Check-Out Date', required=True)
    status = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], string='Status', required=True)
    
