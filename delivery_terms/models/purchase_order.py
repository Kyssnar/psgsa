# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import AccessDenied


class PurchasOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_terms_id = fields.Many2one('delivery.terms',string='Delivery Terms', required=True)
    po_types_id = fields.Many2one('po.types',string='PO Types', required=True)
    po_kinds_id = fields.Many2one('po.kinds',string='PO Kinds', required=True)


class PurchasOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    delivery_terms_id = fields.Many2one(related='order_id.delivery_terms_id', string='Delivery Terms',)
    po_types_id = fields.Many2one(related='order_id.po_types_id', string='PO Types',)
    po_kinds_id = fields.Many2one(related='order_id.po_kinds_id', string='PO Kinds',)