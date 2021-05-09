# -*- coding: utf-8 -*-
{
    'name': 'Open Academy',

    'summary': """Learning Odoo""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': 'CJ',
    'website': 'https://carlosjoel.net',

    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'views/session_board.xml',
        'reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
