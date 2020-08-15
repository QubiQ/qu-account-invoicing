# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale & Invoice General Discount",
    "summary": "Sale & Invoice General Discount",
    "version": "13.0.1.0.0",
    "category": "Custom",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "account",
        "sale",
    ],
    "data": [
        "views/sale_order_view.xml",
        "views/sale_order_document.xml",
        "views/account_move_view.xml",
        "views/account_move_document.xml",
    ],
}
