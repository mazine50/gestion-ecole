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
