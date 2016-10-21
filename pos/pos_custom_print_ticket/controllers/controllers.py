# -*- coding: utf-8 -*-
from openerp import http

# class PosCustomPrintTicket(http.Controller):
#     @http.route('/pos_custom_print_ticket/pos_custom_print_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_custom_print_ticket/pos_custom_print_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_custom_print_ticket.listing', {
#             'root': '/pos_custom_print_ticket/pos_custom_print_ticket',
#             'objects': http.request.env['pos_custom_print_ticket.pos_custom_print_ticket'].search([]),
#         })

#     @http.route('/pos_custom_print_ticket/pos_custom_print_ticket/objects/<model("pos_custom_print_ticket.pos_custom_print_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_custom_print_ticket.object', {
#             'object': obj
#         })