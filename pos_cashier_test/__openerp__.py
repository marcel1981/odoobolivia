# -*- coding: utf-8 -*-
{
    'name': "POS cashiers",

    'summary': """
        Manage cashiers for Point Of Sale""",

    'description': """
        Manage several cashiers for each Point Of Sale
        ======================================

        This could be handy in case of using the same POS at the same cash register while it is used by several cashiers.
        Cashier's name is displayed on the payement receipt and on the order.

        Cashiers are allowed to change the current cashier (by choosing their name in the drop-down list) and can make a sell without creating a new session.

        Cashier's name is mandatory. You cannot perform a sell if no cashier has been created or is active in your POS.

        The shop manager will know who made the sell.
    """,

    'author': "Thierry Godin",
    'update': "Ivan Carvajal",
    'website': "http://www.boliviacic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'sequence': '3',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [        
        'views/views.xml',
        'views/order_cashier_view.xml',
    ],
    'js': [
        'static/src/js/pos_cashier.js',
    ],
    'css': [
        'static/src/css/pos_cashier.css',
    ],
    'qweb': [
        'static/src/xml/pos_cashier.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,   
}