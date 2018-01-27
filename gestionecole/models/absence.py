# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _


class Absence(models.Model):
    _name = 'gestionecole.absence'
    
    etudiant_id = fields.Many2one('gestionecole.etudiant', string="Etudiant")
    matier_id = fields.Many2one('gestionecole.matiere', string="Matier")
    date = fields.Date(default=fields.Date.today)
