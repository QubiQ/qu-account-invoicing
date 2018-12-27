# Copyright 2018 <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Expiration Notification",
    "summary": "Reminder of the payments by email of the payments of the week if in the method of payment is indicated.",
    "version": "11.0.1.0.0",
    "category": "Custom",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "purchase",
        "mail",
        "account_payment_mode"
    ],
    "data": [
        "data/account_exp_cron.xml",
        "data/email_template_acc_not.xml",
        "views/account_payment_mode.xml"
    ],
}
