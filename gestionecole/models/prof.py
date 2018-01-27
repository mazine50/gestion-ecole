# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Professeur(models.Model):
    _name = 'gestionecole.professeur'
    
    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    email = fields.Char(string="Email", required=False)
    telephone = fields.Integer(string="Telephone", required=False)
