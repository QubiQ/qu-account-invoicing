# -*- coding: utf-8 -*-
# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Related Invoice Date Warning",
    "summary": "Invoice Date Check Warning",
    "version": "10.0.1.0.0",
    "category": "Invoicing",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "depends": [
        "account"
    ],
    "data": [
        "views/account_invoice.xml",
        "wizards/invoice_date_warning.xml",
    ],
    "application": False,
    "installable": True,
}
