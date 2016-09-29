# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import time, datetime



class empleado(models.Model):
     _name = 'empleado.empleado'

     name = fields.Char(string="Nombre Completo", required=True,help="Ingrese su nombre Completo")
     ci = fields.Integer(string="Carnet de Identidad", required=True)
     edad = fields.Integer(string="Edad")
     direccion = fields.Text(string="Direccion", required=True)
     telefono = fields.Integer(string="Telefonos", required=True)
     active = fields.Boolean(string="Activo")
     state = fields.Selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')],'Estado',default='draft')

     _sql_constraints = [('ci_emision_unique', 'unique(ci,edad)', "Error! This Type already exists!")]     

class cargo(models.Model):
    _name = 'empleado.cargo'
    
    name = fields.Char(string='Nombre del Cargo', required=True)
    salario = fields.Float(digits=(6,2),help='Salario segun el cargo')
    fecha_inicial = fields.Date()
    cliente_id = fields.Many2one('res.partner','Cliente', required=True)
    empleado = fields.Many2one('empleado.empleado','Empleado')
    
    #_defaults = {
    #    "cliente_id": lambda self, cr, uid, c: c.get('cliente_id', False),
    #}
    
#class res_partner(models.Model):            
#    _inherit = 'res.partner'
    
#    ci = fields.Integer('Carnet de Identidad', required=True)
