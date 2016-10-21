# -*- coding: utf-8 -*-
{
    'name': "pos_custom_print_ticket",

    'summary': """
        Se cambiara la hoja de estilo para personalizar el tamaño de la impresion.""",

    'description': """
        Custom printer Ticket
    """,

    'author': "Ivan Carvajal",
    'website': "http://www.boliviacic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',        
    ],
    'qweb': ['static/src/xml/pos.xml'],    
}