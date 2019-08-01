# Copyright 2019 Juan Antonio Alfonso <ja.alfonso@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Follow-up Reports",
    "summary": "Follow-up Reports",
    "version": "12.0.1.0.1",
    "category": "Invoicing",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "account_accountant",
        "account_reports",
    ],
    "data": [
        "views/report_followup.xml",
    ],
}
