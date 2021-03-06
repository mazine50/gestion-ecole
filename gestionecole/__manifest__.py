# -*- coding: utf-8 -*-
{
    'name': "Gestion Absence",

    'summary': """Une App qui vous aide a bien gere les absence d'etudiant de votre ecole""",
    'sequence': 3,
    'description': """
        Gestion d'ecole module pour gere l'absence de l'etudiant:
            - etudient enregistrement
            - annees universite 
            - groupe de l'etudient
            - inscription
            - professeur
            - matier
            - absence
    """,

    'author': "Mazine EL HALOUI",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ecole,Productivity,Project,all',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',       
        'views/etudiant.xml',
        'views/annesuniversitaire.xml',
        'views/groupe.xml',
        'views/inscrire.xml',
        'views/prof.xml',
        'views/matier.xml',
        'views/absence.xml',
        'views/absence_board.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'price': 80,
    'currency': 'EUR',
    'license': 'AGPL-3',
    'application': True,
}