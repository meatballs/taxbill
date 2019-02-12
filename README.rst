.. image:: https://travis-ci.org/meatballs/taxbill.svg?branch=master
    :target: https://travis-ci.org/meatballs/taxbill

Taxbill
=======
A tax calculator and optimiser for UK freelancers who provide their services
via a limited company which they own.

Installation
------------

This library requires Python 3.6 or greater.

The simplest way to install it is::

    $ pip install taxbill

Quick Start
-----------

Calculate the taxes you will pay and/or save using::

    $ taxbill calculate

View how to minimise the tax you will pay using::

    $ taxbill optimise

Each option can be passed on the command line. e.g.::

    $ taxbill optimise --requirement=30000 --pension=10000 --year=2019

You can view the options available with::

    $ taxbill calculate --help

or::

    $ taxbill optimise --help

Disclaimer
----------
Use this software at your own risk. Doing so should not be considered financial
or legal advice and the author makes no guarantee or promise as to any results
that might be obtained from its use.
