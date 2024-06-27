from odoo import models, fields

class HotelBilling(models.Model):
    _name = 'hotel.billing'
    _description = 'Hotel Billing'

    reservation_id = fields.Many2one('hotel.reservation', string='Reservation', required=True)
    total_amount = fields.Float('Total Amount', required=True)
    billing_date = fields.Datetime('Billing Date', default=fields.Datetime.now)
    status = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid')
