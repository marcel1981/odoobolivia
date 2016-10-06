# -*- coding: utf-8 -*-
{
    'name': "pos_ticket_custom_bo",

    'summary': """
        Modulo para personalizar el Ticket del POS""",

    'description': """
        Modulo para configurar el tamaño de la impresion, y seleccionar los campos a ser impresos
    """,

    'author': "Ivan Carvajal",
    'website': "http://www.boliviacic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',        
    ],
    'qweb': ['static/src/xml/pos_ticket.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,      
}