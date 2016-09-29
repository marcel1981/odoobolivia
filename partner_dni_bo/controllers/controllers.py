# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (c) 2016 - Scientific research community in Bolivia. All Rights Reserved
#    Author: <ivanmcaa@hotmail.com>
#    Website: www.boliviacic.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of the GNU General Public License is available at:
#    <http://www.gnu.org/licenses/gpl.html>.
#
##############################################################################
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