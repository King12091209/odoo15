from odoo import models, fields

class HotelStaff(models.Model):
    _name = 'hotel.staff'
    _description = 'Hotel Staff'

    name = fields.Char('Staff Name', required=True)
    position = fields.Selection([('receptionist', 'Receptionist'), ('concierge', 'Concierge'), ('housekeeping', 'Housekeeping')], required=True)
    hire_date = fields.Date('Hire Date')
    salary = fields.Float('Salary')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], default='active')
