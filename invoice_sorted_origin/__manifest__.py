# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice Sorted Origin',
    'version': '11.0.1.0.0',
    'sequence': 1,
    'summary': 'Orders invoice lines by their origin.',
    'author': 'QubiQ SL',
    'website': 'https://www.qubiq.es',
    'depends': [
                'base',
                'account_invoicing',
                ],
    'category': 'Custom',
    'data': [
                'reports/sorted_report_invoice.xml',
            ],
    'installable': True,
    'application': False,
}
