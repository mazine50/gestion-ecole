# -*- coding: utf-8 -*-
from datetime import timedelta
import time
from odoo import models, fields, api, exceptions, _


class Absence(models.Model):
    
    _name = 'gestionecole.absence'
    
    etudiant_id = fields.Many2one('gestionecole.etudiant', string="Etudiant")
    matier_id = fields.Many2one('gestionecole.matiere', string="Matier")
    date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help=_("Duration in days"))
    color = fields.Integer()
    """calendar"""
    end_date = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date')
    
   
    """calendar"""       
    @api.depends('date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.date and r.duration):
                r.end_date = r.date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            date = fields.Datetime.from_string(r.date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - date).days + 1
