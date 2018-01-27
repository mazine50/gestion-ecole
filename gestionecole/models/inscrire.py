# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _


class Inscrire(models.Model):
    _name = 'gestionecole.inscrire'
    
    incrire = fields.Date(default=fields.Date.today)
    etudiant_id = fields.Many2one('gestionecole.etudiant', string="Etudiant")
    anneeuni_id = fields.Many2one('gestionecole.annesuniversitaire', string="Annees Univesitare")
    groupe_id = fields.Many2one('gestionecole.groupe', string="Groupe")
    