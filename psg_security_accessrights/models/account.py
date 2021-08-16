from openerp import models, fields, api,SUPERUSER_ID

from odoo.exceptions import ValidationError

from lxml import etree

class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

        res = super(AccountAnalyticAccount, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                      submenu=False)
        # print("res",res)

        # group_id = self.env.user.has_group('account.group_account_user')
        group_id = self.env.user.has_group('psg_security_accessrights.show_button_create_analytical_account')
        print("group_id", group_id)
        doc = etree.XML(res['arch'])
        print("doc", doc)

        # if group_id and self.env.uid != 2:
        # if group_id and not self.env.user.has_group('base.group_system') and self.env.uid != SUPERUSER_ID:
        if group_id:
            print("gggggggg", view_type)

            if view_type == 'tree' or view_type == 'form' or view_type == 'search':
                print("111111111111111", view_type)

                nodes_tree = doc.xpath("//tree[@string='Analytic Accounts']")

                for node in nodes_tree:
                	node.set('create', '0')
                	node.set('edit', '0')

                nodes_form = doc.xpath("//form[@string='Analytic Account']")
                print("nodes_form", nodes_form)

                for node in nodes_form:
                    node.set('create', '0')
                    node.set('edit', '0')
                res['arch'] = etree.tostring(doc)

        return res


class AccountAccount(models.Model):
    _inherit = 'account.account'

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

        res = super(AccountAccount, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                      submenu=False)
        # print("res",res)

        # group_id = self.env.user.has_group('account.group_account_user')
        group_id = self.env.user.has_group('psg_security_accessrights.show_button_create_chart_of_account')
        print("group_id", group_id)
        doc = etree.XML(res['arch'])
        print("doc", doc)

        # if group_id and self.env.uid != 2:
        # if group_id and not self.env.user.has_group('base.group_system') and self.env.uid != SUPERUSER_ID:
        if group_id:
            print("yyyyyyyy", view_type)

            if view_type == 'tree' or view_type == 'form' or view_type == 'search':
                print("222222222222", view_type)

                nodes_tree = doc.xpath("//tree[@string='Chart of accounts']")

                for node in nodes_tree:
                	node.set('create', '0')
                	node.set('edit', '0')

                nodes_form = doc.xpath("//form[@string='Account']")
                print("nodes_form", nodes_form)

                for node in nodes_form:
                    node.set('create', '0')
                    node.set('edit', '0')
                # res['arch'] = etree.tostring(doc)

                nodes_kanban = doc.xpath('//kanban[1]')
                print("nodes_kanban", nodes_kanban)

                for node in nodes_kanban:
                    node.set('create', '0')
                    node.set('edit', '0')
                res['arch'] = etree.tostring(doc)

        return res

