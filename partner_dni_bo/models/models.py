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

from openerp import models, fields, api
from lib2to3.fixer_util import String

class partner_dni_bo(models.Model):
    _inherit = 'res.partner'
    
    ci = fields.Char(string='Carnet de Identidad',required=True)
    emision = fields.Many2one('res.country.state', string='Emitido en',required=True)
    vat = fields.Char(string='NIT')    

    _sql_constraints = [('ci_emision_unique', 'unique(ci,emision)', "Error: Cliente ya registrado!")]    
    
    _defaults = { 
        'country_id': lambda self, cr, uid, context: self.pool.get('res.country').browse(cr, uid, self.pool.get('res.country').search(cr, uid, [('code','=','BO')]))[0].id,
        'state_id': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','LP')]))[0].id,
        'emision': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','LP')]))[0].id,
        'city': 'El Alto',
        'zip': 'LP',
        }