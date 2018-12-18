.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

================================
Partner Invoice Analytic Account
================================

Allows to set an analytic account for sales and another one for purchases for every partner. Those accounts will be used by default on orders and invoices.


Installation
============

Just install.


Configuration
=============

Go to Sales -> Orders -> Customers, choose a partner and set the "Sales Analytic Account" and "Purchases Analytic Account" under the Sales and Purchases tab. The functionality of this module is company dependent.


Usage
=====

On sale orders, when the partner is chosen the specified analytic account is transferred to the order.
When the invoice is created from the sale order, its analytic account is transferred to every invoice line.
If an invoice is created without a sale order or a purchase order, the analytic account will be taken directly from the partner.


ROADMAP
=======

* ...


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/QubiQ/qu-account-invoicing/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/QubiQ/qu-account-invoicing/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* QubiQ, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Xavier Piernas <xavier.piernas@qubiq.es>
* Valentín Vinagre <valentin.vinagre@qubiq.es>


Maintainer
~~~~~~~~~~

This module is maintained by QubiQ.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: QubiQ
   :target: https://www.qubiq.es

This module is part of the `QubiQ/qu-account-invoicing <https://github.com/QubiQ/qu-account-invoicing>`_.

To contribute to this module, please visit https://github.com/QubiQ.