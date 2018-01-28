# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Etudiant(models.Model):
    _name = 'gestionecole.etudiant'
    
    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    ville = fields.Char(string="Ville", required=False)
    sex = fields.Selection((('M','Male'),('F','Female'),('A','Autre')))
    date_naissance = fields.Date()
    email = fields.Char(string="Email", required=False)
    address = fields.Char(string="Address", required=False)
    telephone_perso = fields.Integer(string="Telephone personnel", required=False)
    telephone_parent = fields.Integer(string="Telephone parent", required=False)

    _sql_constraints = [
        ('telephone_perso_telephone_parent_check',
         'CHECK(telephone_perso != telephone_parent)',
         _("le numero de l'etudiant doit etre différent du numero parent")),

        ('telephone_perso_unique',
         'UNIQUE(telephone_perso)',
         "le numero personnel de l'etudiant doit etre unique"),
        
        ('telephone_parent_unique',
         'UNIQUE(telephone_parent)',
         "le numero parent doit etre unique"),
    ]
    
    
