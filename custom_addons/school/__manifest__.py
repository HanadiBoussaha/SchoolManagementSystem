# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School management',
    'version': '1.8',
    'category': 'School',
    'description':'This module allows you to manage a school',
    'summary': 'This module allows you to manage a school',
    'author': 'chaima Hanadi',
    'website': 'https://erptogo.net',
    'license': 'LGPL-3',
    'depends': [
        'base_setup','mail','web'
    ],

    'data': [
     'security/ir.model.access.csv',
     'views/student_view.xml',
     'views/student_class_view.xml',
     'views/school_cours_view.xml',
     'reports/student_report.xml',
    ],

    'installable': True,
    'application': False,
    'sequence':'0',

}
