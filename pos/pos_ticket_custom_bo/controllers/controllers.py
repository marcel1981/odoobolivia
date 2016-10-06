# -*- coding: utf-8 -*-
from openerp import http

# class PosTicketCustomBo(http.Controller):
#     @http.route('/pos_ticket_custom_bo/pos_ticket_custom_bo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_ticket_custom_bo/pos_ticket_custom_bo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_ticket_custom_bo.listing', {
#             'root': '/pos_ticket_custom_bo/pos_ticket_custom_bo',
#             'objects': http.request.env['pos_ticket_custom_bo.pos_ticket_custom_bo'].search([]),
#         })

#     @http.route('/pos_ticket_custom_bo/pos_ticket_custom_bo/objects/<model("pos_ticket_custom_bo.pos_ticket_custom_bo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_ticket_custom_bo.object', {
#             'object': obj
#         })