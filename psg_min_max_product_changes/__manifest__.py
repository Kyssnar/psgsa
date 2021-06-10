# -*- coding: utf-8 -*-
{
    'name': "psg_min_max_product_changes",
    'summary': """
        Required Modifications to Add Min Max Qty Fields To Product Modele Based on Local Staff requirements
    """,
    'description': """
        - Add Field Min Max To Product Card Screen .
        - Show Min ,Max ,On Hand values In purchase Request product lines .
        - Show Min ,Max ,On Hand values In purchase orders product lines .
    """,
    'author': "psg technical team | Tal3at Elbedwihi",
    'website': "https://primesourcegroup.com.sa/",
    'category': 'Inventory/Purchase',
    'version': '1.0',
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': ['base','purchase','product','purchase_request'],
    'data': [
        'views/product_template.xml',
        'views/purchase_request.xml',
        'views/purchase_order_line.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}