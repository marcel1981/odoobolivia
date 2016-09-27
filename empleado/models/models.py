# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import time, datetime
from email import _name
from encodings.punycode import digits
from pychart.arrow import default
from pkg_resources import require
from pygments.lexer import _inherit


class empleado(models.Model):
     _name = 'empleado.empleado'

     name = fields.Char(string="Nombre Completo", required=True,help="Ingrese su nombre Completo")
     ci = fields.Integer(string="Carnet de Identidad", required=True)
     edad = fields.Integer(string="Edad")
     direccion = fields.Text(string="Direccion", required=True)
     telefono = fields.Integer(string="Telefonos", required=True)
     active = fields.Boolean(string="Activo")
     state = fields.Selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')],'Estado',default='draft')

class cargo(models.Model):
    _name = 'empleado.cargo'
    
    name = fields.Char(string='Nombre del Cargo', required=True)
    salario = fields.Float(digits=(6,2),help='Salario segun el cargo')
    fecha_inicial = fields.Date()
    cliente_id = fields.Many2one('res.partner','Cliente', required=True)
    empleado = fields.Many2one('empleado.empleado','Empleado')
    
class res_partner(models.Model):            
    _inherit = 'res.partner'
    
    ci = fields.Integer('Carnet de Identidad', required=True)