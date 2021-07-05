# -*- coding: utf-8 -*-
{
    'name': "psg_stock_picking_weight",
    'summary': """
        Required Modifications to Enhance stock picking based on Local Staff requirements
    """,
    'description': """
        - Add Field Invoice weight to stock picking .
        - Add Field Actual weight to stock picking .
        - Add Field Difference to stock picking .
    """,
    'author': "psg technical team | Tal3at Elbedwihi",
    'website': "https://primesourcegroup.com.sa/",
    'category': 'Inventory',
    'version': '1.0',
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': ['base','stock'],
    'data': [
        'views/stock_picking.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}