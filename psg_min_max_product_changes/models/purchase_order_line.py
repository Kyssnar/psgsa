from odoo import models, fields, api


class ModifyPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Add Fields To Purchase Order Line Model'

    min_qty = fields.Float(string='Min Qty', related='purchase_request_lines.min_qty', default=0.0)
    max_qty = fields.Float(string='Max Qty', related='purchase_request_lines.max_qty', default=0.0)
    on_hand = fields.Float(string='On Hand', related='purchase_request_lines.product_id.qty_available', default=0.0)