# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Merge Account Menu',
    'version': '13.0.1.0.0',
    'category': 'Custom',
    'summary': "Merge the two accountant menus when installing l10n_es_aeat on EE",
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends':  [
        'account_accountant',
        'l10n_es_aeat'
    ],
    'data': [
        'data/menu.xml'
    ],
    'auto_install': True,
    'installable': True,
}
