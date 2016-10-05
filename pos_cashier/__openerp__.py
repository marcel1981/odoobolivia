# -*- coding: utf-8 -*-
#
# Slavishly copied from Thierry Godin tutorial on the web
# http://thierry-godin.developpez.com/openerp/tutorial-module-creation-pos-modification-english-version/
#

{
    'name': 'POS Cashiers',
    'version': '1.0.0',
    'category': 'Point Of Sale',
    'sequence': 3,
    'author': 'Thierry Godin',
    'summary': 'Manage cashiers for Point Of Sale',
    'description': """
Manage several cashiers for each Point Of Sale
==============================================

This could be handy in case of using the same POS at the same cash register while it is used by several cashiers.
Cashier's name is displayed on the payement receipt and on the order.

Cashiers are allowed to change the current cashier (by choosing their name in the drop-down list) and can make a sell without creating a new session.

Cashier's name is mandatory. You cannot perform a sell if no cashier has been created or is active in your POS.

The shop manager will know who made the sell.
    """,
    'depends': ["point_of_sale"],
    'data': [
        'security/pos_cashier_security.xml',
        'security/ir.model.access.csv',
        'cashier_view.xml',
        'order_cashier_view.xml',
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