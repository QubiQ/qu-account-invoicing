.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

======================
Indirect Cost Invoices
======================

This module calculates the Indirect Cost for Sale Invoice Lines during a time period based on a given Purchase Invoice.


Installation
============

No special installation is required.


Configuration
=============

No special configuration is required.


Usage
=====

To use this module, you need to:

#. Create a purchase invoice, validate it and set its state to done.
#. Create one or more purchase orders for one or more products from the previous purchase invoice, validate them and set their state to done.
#. Access the "Indirect Cost Invoices" menu from Invoicing/Adviser/Indirect Cost Invoices
#. Create a new Indirect Cost Invoice.
#. Select a Purchase Order Invoice, a Type Search for Products or Product Categories and a Date Period of the sale invoices.
#. Select costumers for the Invoice Lines and Products or Product Categories.
#. Save and press Apply.
#. The average unit cost will be calculated and applied to the extra cost of the invoice lines.
#. The information from the modified Sale Order Lines will appear in a new tab called "Invoice Lines".
#. To undo the changes made to the extra cost of the Invoice Lines, press "Cancel".

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

* Valentin Vinagre <valentin.vinagre@qubiq.es>
* Oscar Navarro <oscar.navarro@qubiq.es>


Maintainer
~~~~~~~~~~

This module is maintained by QubiQ.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: QubiQ
   :target: https://www.qubiq.es

This module is part of the `QubiQ/REPOSITORY <https://github.com/QubiQ/repository>`_.

To contribute to this module, please visit https://github.com/QubiQ.
