# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class PoKinds(models.Model):
    _name = 'po.kinds'
    _rec_name = 'name'

    name = fields.Char("Name" ,required=True)
    description = fields.Text("Description")
