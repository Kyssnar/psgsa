# -*- coding: utf-8 -*-

{
    'name': 'Delivery Terms',
    'category': 'Purchases',
    'summary': 'This module will add delivery terms to Purchase Orders',
    'version': '14.0.1.0.0',
    'author': 'Ahmed Gaber',
    'description': 'This module will add delivery terms to Purchase Orders',
    'license': "AGPL-3",

    'depends': ['purchase', 'stock','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_terms_view.xml',
        'views/po_types_view.xml',
        'views/po_kinds_view.xml',
        'views/purchase_order.xml',
        'views/stock_view.xml',
        'views/account_view.xml',

    ],

    'auto_install': False,
    'installable': True,
    'application': False

}
