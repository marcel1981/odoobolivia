# -*- coding: utf-8 -*-
{
    'name': "pos_custom_partner_bo",

    'summary': """
        Añadir los campos C.I. y Departamento en el formulario del POS de registro de Clientes.
    """,

    'description': """
        Ampliar el formulario de registro de Clientes del Punto de Venta, añadir los campos C.I. y departamento de emision                
    """,

    'author': "Labcit",
    'website': "http://www.labcit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',        
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,   
}