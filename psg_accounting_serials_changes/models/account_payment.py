from odoo import models, fields, api


class ModifyAccountPayment(models.Model):
    _inherit = 'account.payment'
    _description = 'Add Fields To Account Payment'

    source_journal = fields.Many2one('account.source_journal', string='Source Journal', required=True)
    source_document = fields.Many2one('account.document_serials', string='Source Document', required=True,
                                      domain="[('source_journal','=',source_journal),('is_related','=',False)]")

    def unlink(self):
        self.env["account.document_serials"].search([('id', '=', self.source_document.id)]).write(
            {
                "is_related": False
            }
        )
        res = super().unlink()
        return res

    @api.model
    def create(self, vals):
        result = super(ModifyAccountPayment, self).create(vals)
        self.env["account.document_serials"].search([('id', '=', vals.get("source_document"))]).write(
            {
                "is_related": True
            }
        )
        return result