from odoo import models, fields, api


class ModifyPurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    _description = 'Add Fields To Purchase Request Line Model'

    min_qty = fields.Float(string='Min Qty', related='product_id.min_qty', default=0.0)
    max_qty = fields.Float(string='Max Qty', related='product_id.max_qty', default=0.0)
    on_hand = fields.Float(string='On Hand', related='product_id.qty_available', default=0.0)