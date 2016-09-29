# -*- coding: utf-8 -*-

from openerp import models, fields, api

class partner_dni_bo(models.Model):
    _inherit = 'res.partner'
    
    ci = fields.Char(string='Carnet de Identidad',required=True)
    emision = fields.Many2one('res.country.state', string='Emitido en',required=True)    

    _sql_constraints = [('ci_emision_unique', 'unique(ci,emision)', "Error: Cliente ya registrado!")]    
    
    _defaults = { 
        'country_id': lambda self, cr, uid, context: self.pool.get('res.country').browse(cr, uid, self.pool.get('res.country').search(cr, uid, [('code','=','BO')]))[0].id,
        'state_id': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','LP')]))[0].id,
        'emision': lambda self, cr, uid, context: self.pool.get('res.country.state').browse(cr, uid, self.pool.get('res.country.state').search(cr, uid, [('code','=','LP')]))[0].id,
        'city': 'El Alto',
        'zip': 'LP',
        }