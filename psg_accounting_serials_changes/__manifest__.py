# -*- coding: utf-8 -*-
{
    'name': "psg_accounting_serials_changes",
    'summary': """
        Required Modifications to add Document Serials & Source Journals 
    """,
    'description': """
        - Create Screen Source Journals .
        - Create Screen Document Serials .
        - Add Related Fields to payments Screen .
    """,
    'author': "psg technical team | Tal3at Elbedwihi",
    'website': "https://primesourcegroup.com.sa/",
    'category': 'Accounting/Accounting',
    'version': '1.0',
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': ['base','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/source_journal.xml',
        'views/document_serials.xml',
        'views/account_payment.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
