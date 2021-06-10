from odoo import models, fields, api


class ModifyPurchaseOrder(models.Model):
    _inherit = 'product.template'
    _description = 'Add Fields To product template Model'

    min_qty = fields.Float(string='Minimum Qty', default=0.0)
    max_qty = fields.Float(string='Maximum Qty', default=0.0)