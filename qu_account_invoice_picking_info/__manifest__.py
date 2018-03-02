# -*- coding: utf-8 -*-

{
    'name': 'Account Invoice picking Info',
    'version': '10.0.1.0.0',
    'sequence': 14,
    'summary': 'Custom',
    'description': """
Account Invoice picking Info
============================

Shows picking number on invoice report

    """,
    'author': 'QubiQ SL',
    'website': 'https://www.qubiq.es',
    'depends': [
                'account',
                'stock_picking_invoice_link',
                ],
    'category': 'Custom',
    'data': [
                'reports/report_invoice.xml',

            ],
    'demo': [],
    'installable': True,
}
