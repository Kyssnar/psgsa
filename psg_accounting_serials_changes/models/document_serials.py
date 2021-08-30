from odoo import models, fields, api
from lxml import etree


class AccountDocumentSerials(models.Model):
    _name = 'account.document_serials'
    _description = 'document serials'
    _order = "id"

    name = fields.Char(string='Serial')
    source_journal = fields.Many2one('account.source_journal', string='Source Journal')
    is_related = fields.Boolean("Is Related")

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(AccountDocumentSerials, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                                           toolbar=toolbar, submenu=submenu)
        root = etree.fromstring(res['arch'])
        root.set('create', 'false')
        root.set('edit', 'false')
        res['arch'] = etree.tostring(root)
        return res
