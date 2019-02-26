# -*- coding: utf-8 -*-
# Copyright 2019 Valentin Vinagre Urteaga <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Invoice Journal",
    "summary": "Define journals for sales and purchases for the invoices.",
    "version": "10.0.1.0.0",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "account",
        "purchase",
    ],
    "data": [
        "views/res_partner.xml",
    ],
}
