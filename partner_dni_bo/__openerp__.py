# -*- coding: utf-8 -*-
{
    'name': "Extend Partner CI, Department",

    'summary': """
        English: Extend the functionality of object Partner.
        Spanish: Extender la funcionalidad del objeto Partner.
        """,

    'description': """
        English: This module was developed to add identity card and identification for Department where Bolivia was issued fields, Bolivia also establishes default when registering a client.
        
        Spanish: Este modulo se desarrollo para añadir los campos Carnet de Identidad y Departamento donde se emitio la identificacion para Bolivia, tambien establece por defecto Bolivia al momento de registrar un cliente.
        
        Restriccion: C.I. y Departamento son un identificador unico: _sql_constraints = [('unique_fields', 'unique(ci,emision), 'Error! This Type already exists!')].
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