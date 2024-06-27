from odoo import http
from odoo.http import request

class WebsiteReservation(http.Controller):

    @http.route('/hotel/reservation', auth='public', website=True)
    def hotel_reservation(self, **kwargs):
        rooms = request.env['hotel.room'].search([])
        return request.render('hotel_management.hotel_reservation_template', {
            'rooms': rooms
        })

    @http.route('/hotel/reservation/submit', type='http', auth='public', website=True, methods=['POST'])
    def submit_reservation(self, **post):
        request.env['hotel.reservation'].create({
            'customer_id': int(post.get('customer_id')),
            'room_id': int(post.get('room_id')),
            'check_in': post.get('check_in'),
            'check_out': post.get('check_out'),
            'status': 'pending'
        })
        return request.redirect('/hotel/reservation')
