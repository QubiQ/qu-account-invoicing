# Copyright 2020 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Invoice Validation Confirmation",
    "summary": "Asks for confirmation to validate invoices with no amount",
    "version": "11.0.1.0.0",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
       "account"
    ],
    "data": [
        "views/account_invoice.xml"
    ]
}
