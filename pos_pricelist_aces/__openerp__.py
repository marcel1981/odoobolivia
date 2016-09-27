# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (c) 2012 - Present Acespritech Solutions Pvt. Ltd. All Rights Reserved
#    Author: <info@acespritech.com>
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
    'name': 'Point of Sale PriceList',
    'version': '1.0',
    'category': 'Point of Sale',
    'author': "Acespritech Solutions Pvt. Ltd.",
    'website': 'http://www.acespritech.com',
    'description': "Apply pricelist from Point Of Sale Interface",
    'summary': 'Apply pricelist from Point Of Sale Interface',
    'currency': 'EUR',
    'price': 9.00,
    'depends': ['web', 'point_of_sale'],
    'images': ['static/description/main_screenshot.png'],
    'data': [
        'views/pos_pricelist.xml',
        'point_of_sale/pos_view.xml'
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: