# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Psvalliance Website',
    'version' : '1.0',
    'summary': 'Sample Website',
    'author': 'Odoo.',
    'sequence': 30,
    'description': """
Sample Website
====================
For Clinic Information Maintenance
    """,
    'category': 'website',
    'website': 'http://newwaveoffices.com/',
    'depends': [
    ],
    'data': [
        'views/website_templates.xml',
        'views/subscribers.xml',
        'views/clients.xml',
        'views/vendors.xml',
        'views/menu.xml',
    ],
    #'demo': [
    #    'views/fpt_menus_ept.xml',
    #],
    #'qweb': [
    #    "static/src/xml/account_reconciliation.xml",
    #    "static/src/xml/account_payment.xml",
    #    "static/src/xml/account_report_backend.xml",
    #],
    'installable': True,
    'application': True,
    'auto_install': False,
}