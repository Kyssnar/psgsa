from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountSourceJournal(models.Model):
    _name = 'account.source_journal'
    _description = 'source journal'
    _order = "id"

    name = fields.Char(string='Journal Number', readonly=True, required=True, copy=False, default='Draft JN')
    number_of_documents = fields.Integer(string='No of Documents', required=True, default=0)
    serial_from = fields.Integer(string='Serial From', required=True, default=0)
    serial_to = fields.Integer(string='Serial To', readonly=True, required=True, default=0)
    note = fields.Text(string='Note')

    def write(self, vals):
        if self.env['account.document_serials'].search([('source_journal', '=', self.id), ('is_related', '=', True)]).id > 0:
            return {
                'warning': {
                    'title': 'Notification Message',
                    'message': 'Unable to update, this source journal has related serials used .',
                }
            }
        else:
            self.env['account.document_serials'].search([('source_journal', '=', self.id)]).unlink()
            for x in range(vals.get('serial_from', self.serial_from),
                           (vals.get('serial_from', self.serial_from) +
                            vals.get('number_of_documents', self.number_of_documents))):
                self.env["account.document_serials"].create(
                    {
                        "name": x,
                        "source_journal": self.id,
                        "is_related": False
                    }
                )
            vals['serial_to'] = vals.get('serial_from', self.serial_from) + vals.get('number_of_documents',
                                                                                     self.number_of_documents) - 1
            res = super(AccountSourceJournal, self).write(vals)
            return res

    def unlink(self):
        if self.env['account.document_serials'].search([('source_journal', '=', self.id), ('is_related', '=', True)]).id > 0:
            return {
                'warning': {
                    'title': 'Notification Message',
                    'message': 'Unable to delete, this source journal has related serials used .',
                }
            }
        else:
            self.env['account.document_serials'].search([('source_journal', '=', self.id)]).unlink()
            res = super().unlink()
            return res

    def action_document_serials(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Document Serials',
            'res_model': 'account.document_serials',
            'domain': [('source_journal', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current'
        }

    @api.model
    def create(self, vals):
        if vals.get('name', 'Draft JN') == 'Draft JN':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.journal_number') or 'Draft JN'

        vals['serial_to'] = vals['serial_from'] + vals['number_of_documents'] - 1
        result = super(AccountSourceJournal, self).create(vals)
        for x in range(vals['serial_from'], (vals['serial_from'] + vals['number_of_documents'])):
            self.env["account.document_serials"].create(
                {
                    "name": x,
                    "source_journal": str(result).replace("account.source_journal(", "").replace(",)", ""),
                    "is_related": False
                }
            )
        return result


