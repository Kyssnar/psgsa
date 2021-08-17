# -*- coding: utf-8 -*-

{
    'name': "Financial Reports Lines",
    'summary': """Add menu for Financial Reports Lines""",
    'description': """Add menu for Financial Reports Lines""",
    'author': "Ahmed Gaber",
    'license': 'AGPL-3',
    'category': 'account',
    'version': '14.0',
    'depends': ['base','account','account_reports'],
    'data': [
        'views/account_type_view.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': True,
}
