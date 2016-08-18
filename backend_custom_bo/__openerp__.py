# -*- coding: utf-8 -*-
{
    'name': "Plantilla Backend",

    'summary': """
        Plantilla para instalar y configurar Bootswatch""",

    'description': """
        Plantilla para instalar y configurar Bootswatch sobre Odoo
        sera necesario descargar los archivos LESS de Bootswatch
    """,

    'author': "Ivan Carvajal",
    'website': "http://www.boliviabi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',
    
    'images':[
        'static/images/backend.png'
    ],

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    "installable": True,        
}