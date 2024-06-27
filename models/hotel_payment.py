from odoo import models, fields

class HotelPayment(models.Model):
    _name = 'hotel.payment'
    _description = 'Hotel Payment'

    reservation_id = fields.Many2one('hotel.reservation', string='Reservation', required=True)
    amount = fields.Float('Amount', required=True)
    payment_method = fields.Selection([('cash', 'Cash'), ('check', 'Check'), ('credit_card', 'Credit Card')], default='cash')
    payment_date = fields.Datetime('Payment Date', default=fields.Datetime.now)
