# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_delivery_terms(self):

        for move in self:
            if move.origin:
                if move.origin.startswith('P'):
                    main = self.env['purchase.order'].search([('name', '=', move.origin)], limit=1)
                    if main:
                        move.delivery_terms_id = main.delivery_terms_id.id
                        move.po_types_id = main.po_types_id.id
                        move.po_kinds_id = main.po_kinds_id.id
                    else:
                        move.delivery_terms_id = False
                        move.po_types_id = False
                        move.po_kinds_id = False
                else:
                    move.delivery_terms_id = False
                    move.po_types_id = False
                    move.po_kinds_id = False

            else:
                move.delivery_terms_id = False
                move.po_types_id = False
                move.po_kinds_id = False

    delivery_terms_id = fields.Many2one('delivery.terms',string='Delivery Terms',compute='get_delivery_terms')
    po_types_id = fields.Many2one('po.types',string='PO Types',compute='get_delivery_terms')
    po_kinds_id = fields.Many2one('po.kinds',string='PO Kinds',compute='get_delivery_terms')
    # delivery_terms_id = fields.Many2one(related='move_lines.purchase_line_id.order_id.delivery_terms_id',string='Delivery Terms', required=True)


# class StockMove(models.Model):
#     _inherit = 'stock.move'
#
#     delivery_terms_id = fields.Many2one(related='picking_id.delivery_terms_id', string='Delivery Terms',)