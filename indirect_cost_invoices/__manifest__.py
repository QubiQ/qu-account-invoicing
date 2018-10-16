# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Indirect Cost Invoices",
    "summary": "Module summary",
    "version": "11.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/indirect_cost_invoices_view.xml",
    ],
}
