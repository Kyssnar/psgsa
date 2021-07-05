from odoo import models, fields, api

class ModifyStockPicking(models.Model):
    _inherit = 'stock.picking'
    _description = 'Add Fields To stock picking Model'

    invoice_weight = fields.Float(string='Invoice Weight', default=0.0)
    actual_weight = fields.Float(string='Actual Weight', default=0.0)
    difference = fields.Float(string='Difference', compute='_get_wight_difference')

    @api.depends('invoice_weight', 'actual_weight')
    def _get_wight_difference(self):
        self.difference = self.invoice_weight - self.actual_weight