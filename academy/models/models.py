# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = 'Academy Teachers'

    name = fields.Char()
    biography = fields.Html()