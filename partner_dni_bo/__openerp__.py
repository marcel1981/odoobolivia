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
{
    'name': "Extend Partner CI, Department",

    'summary': """
        English: Extend the functionality of object Partner.
        Spanish: Extender la funcionalidad del objeto Partner.
        """,

    'description': """
        English: This module was developed to add identity card and identification for Department where Bolivia was issued fields, Bolivia also establishes default when registering a client.
        
        Spanish: Este modulo se desarrollo para añadir los campos Carnet de Identidad y Departamento donde se emitio la identificacion para Bolivia, tambien establece por defecto Bolivia al momento de registrar un cliente.
        
        Restriccion: C.I. y Departamento son un identificador unico: _sql_constraints = [('ci_emision_unique', 'unique(ci,emision), 'Error: Customer already registered!')].
    """,

    'author': "Ivan Carvajal",
    'website': "http://www.boliviacic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',        
    ],    
}