from odoo import http
from odoo.http import request

class HotelReservationController(http.Controller):
    @http.route('/hotel/reservation', type='http', auth="public", website=True)
    def hotel_reservation_form(self, **kwargs):
        rooms = request.env['hotel.room'].sudo().search([])
        clients = request.env['hotel.client'].sudo().search([])
        return request.render('hotel_management.hotel_reservation_template', {
            'rooms': rooms,
            'clients': clients,
        })

    @http.route('/hotel/reservation/submit', type='http', auth="public", methods=['POST'], website=True)
    def hotel_reservation_submit(self, **kwargs):
        request.env['hotel.reservation'].sudo().create({
            'customer_id': int(kwargs.get('customer_id')),
            'room_id': int(kwargs.get('room_id')),
            'check_in': kwargs.get('check_in'),
            'check_out': kwargs.get('check_out'),
        })
        return request.render('hotel_management.hotel_reservation_thanks', {})
