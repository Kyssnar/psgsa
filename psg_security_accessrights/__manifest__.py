# -*- coding: utf-8 -*-
{
    'name': "psg_security_accessrights",
    'summary': """
        Add Access rights to users screen for [journal entries (Post & Cancel Entry Buttons) - chart of accounts (Create Button) - Analytical Account (Create button)]
    """,
    'description': """
        - Add Access rights to user screen
        - Make Affecting Into entire screens
    """,
    'author': "psg technical team | Tal3at Elbedwihi",
    'website': "https://primesourcegroup.com.sa/",
    'category': 'Access Right',
    'version': '1.0',
    'sequence': 1,
    'license': 'LGPL-3',
    'depends': ['base','account'],
    "data": [
        'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/journal_entry.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}