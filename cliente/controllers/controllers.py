# -*- coding: utf-8 -*-
from openerp import http

# class Cliente(http.Controller):
#     @http.route('/cliente/cliente/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cliente/cliente/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cliente.listing', {
#             'root': '/cliente/cliente',
#             'objects': http.request.env['cliente.cliente'].search([]),
#         })

#     @http.route('/cliente/cliente/objects/<model("cliente.cliente"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cliente.object', {
#             'object': obj
#         })