# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Tax Info Invoice Report",
    "summary": "Show an information text about taxes on invoice reports",
    "version": "12.0.1.0.0",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "base"
    ],
    "data": [
        "views/res_company.xml"
    ],
}
