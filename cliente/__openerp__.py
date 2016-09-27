# -*- coding: utf-8 -*-
{
    'name': "cliente",

    'summary': """
        Modulo de clientes para La Selva""",

    'description': """
        Modulo para el tratamiento de clientes, de la importadora y distribuidora La Selva
    """,

    'author': "Ivan Carvajal",
    'website': "http://www.boliviabi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}