# -*- coding: utf-8 -*-
from openerp import http

# class PartnerDniBo(http.Controller):
#     @http.route('/partner_dni_bo/partner_dni_bo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_dni_bo/partner_dni_bo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_dni_bo.listing', {
#             'root': '/partner_dni_bo/partner_dni_bo',
#             'objects': http.request.env['partner_dni_bo.partner_dni_bo'].search([]),
#         })

#     @http.route('/partner_dni_bo/partner_dni_bo/objects/<model("partner_dni_bo.partner_dni_bo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_dni_bo.object', {
#             'object': obj
#         })