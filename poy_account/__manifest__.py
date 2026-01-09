# -*- coding: utf-8 -*-
{
    'name': "POY Accounting Costumizations",

    'summary': "The module includes the costumizations made to feet the costumer's needs",

    'description': """
Long description of module's purpose
    """,

    'author': "KOLEOS",
    'website': "https://www.koleos.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['poy_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'assets': {},
}

