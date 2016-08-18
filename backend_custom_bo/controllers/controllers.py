# -*- coding: utf-8 -*-
from openerp import http

# class BackendCustomBo(http.Controller):
#     @http.route('/backend_custom_bo/backend_custom_bo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/backend_custom_bo/backend_custom_bo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('backend_custom_bo.listing', {
#             'root': '/backend_custom_bo/backend_custom_bo',
#             'objects': http.request.env['backend_custom_bo.backend_custom_bo'].search([]),
#         })

#     @http.route('/backend_custom_bo/backend_custom_bo/objects/<model("backend_custom_bo.backend_custom_bo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('backend_custom_bo.object', {
#             'object': obj
#         })