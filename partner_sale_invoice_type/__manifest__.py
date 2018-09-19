# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Sale Invoice Type",
    "summary": "Invoice types for sale invoices.",
    "version": "11.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "account",
        "sale",
    ],
    "data": [
        "views/res_partner.xml",
        "views/account_invoice.xml",
    ],
}
