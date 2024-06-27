from odoo import api, models, fields

class HotelClient(models.Model):
    _name = 'hotel.client'
    _description = 'Hotel Client'

    name = fields.Char('Client Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    check_in_date = fields.Datetime('Check-In Date')
    check_out_date = fields.Datetime('Check-Out Date')
    stay_duration = fields.Integer('Stay Duration (days)', compute='_compute_stay_duration')

    @api.depends('check_in_date', 'check_out_date')
    def _compute_stay_duration(self):
        for record in self:
            if record.check_in_date and record.check_out_date:
                delta = record.check_out_date - record.check_in_date
                record.stay_duration = delta.days
            else:
                record.stay_duration = 0
