# -*- coding: utf-8 -*-
from openerp import http

# class Empleado(http.Controller):
#     @http.route('/empleado/empleado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empleado/empleado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empleado.listing', {
#             'root': '/empleado/empleado',
#             'objects': http.request.env['empleado.empleado'].search([]),
#         })

#     @http.route('/empleado/empleado/objects/<model("empleado.empleado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empleado.object', {
#             'object': obj
#         })