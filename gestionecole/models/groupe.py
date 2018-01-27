# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Groupe(models.Model):
    _name = 'gestionecole.groupe'
    
    name = fields.Char(string="Nom du Groupe")
    groupe = fields.Selection((('GI','Genie Informatique'),('M','Managment')))
    etudiant_id = fields.Many2one('gestionecole.etudiant', string="Etudiant")
   