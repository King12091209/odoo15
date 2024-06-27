from odoo import models, fields

class HotelSchedule(models.Model):
    _name = 'hotel.schedule'
    _description = 'Hotel Schedule'

    staff_id = fields.Many2one('hotel.staff', string='Staff', required=True)
    shift_start = fields.Datetime('Shift Start', required=True)
    shift_end = fields.Datetime('Shift End', required=True)
    status = fields.Selection([('scheduled', 'Scheduled'), ('completed', 'Completed'), ('missed', 'Missed')], default='scheduled')
