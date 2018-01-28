# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _


class Annesuniversitaire(models.Model):
    _name = 'gestionecole.annesuniversitaire'
    
    name = fields.Char(string="annees")
    etudiant_id = fields.Many2one('gestionecole.etudiant', string="Etudiant")
    date_debut = fields.Date(default=fields.Date.today)
    date_fin = fields.Date()
    
    _sql_constraints = [
        ('date_debut_date_fin_check',
         'CHECK(date_debut != date_fin)',
         _("la date de debut doit etre different de la date fin")),

    
    ]