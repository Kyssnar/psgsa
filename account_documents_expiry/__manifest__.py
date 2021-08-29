# -*- coding: utf-8 -*-

{
    'name': 'Account Documents Expiry',
    'version': '14.0.1.0.0',
    'summary': """Manages Account Documents With Expiry Notifications.""",
    'description': """Manages Account Documents With Expiry Notifications""",
    'category':'account',
    'author': 'Ahmed Gaber',

    'depends': ['base', 'account','hr'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/document_type_view.xml',
        # 'views/hr_document_template.xml',
        'views/account_document_view.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
