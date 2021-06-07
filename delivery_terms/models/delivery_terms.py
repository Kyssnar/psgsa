# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class DeliveryTerms(models.Model):
    _name = 'delivery.terms'
    _rec_name = 'name'

    name = fields.Char("Name" ,required=True)
    description = fields.Text("Description")
