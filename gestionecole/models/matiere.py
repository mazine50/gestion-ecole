# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Matiere(models.Model):
    _name = 'gestionecole.matiere'
    
    name = fields.Char(string="Nom Du Matiere")
    description = fields.Char(string="Description")
    prof_id = fields.Many2one('gestionecole.professeur', string="Professeur")
    semestre = fields.Selection((('S1','semestre 1'),('S2','semestre 2'),('S3','semestre 3'),('S4','semestre 4'),('S5','semestre 5'),('S6','semestre 6'),('S7','semestre 7'),('S8','semestre 8'),('S9','semestre 9'),('S10','semestre 10')))
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         _("le nom du cours doit etre différent de la description")),

        ('name_unique',
         'UNIQUE(name)',
         _("le nom du cours doit etre unique")),
    ]
    