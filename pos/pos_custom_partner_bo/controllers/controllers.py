# -*- coding: utf-8 -*-
from openerp import http

# class PosCustomPartnerBo(http.Controller):
#     @http.route('/pos_custom_partner_bo/pos_custom_partner_bo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_custom_partner_bo/pos_custom_partner_bo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_custom_partner_bo.listing', {
#             'root': '/pos_custom_partner_bo/pos_custom_partner_bo',
#             'objects': http.request.env['pos_custom_partner_bo.pos_custom_partner_bo'].search([]),
#         })

#     @http.route('/pos_custom_partner_bo/pos_custom_partner_bo/objects/<model("pos_custom_partner_bo.pos_custom_partner_bo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_custom_partner_bo.object', {
#             'object': obj
#         })