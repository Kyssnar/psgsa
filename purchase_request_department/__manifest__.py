# Copyright 2017-2020 Forgeflow S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Purchase Request Department",
    "author": "Ahmed Gaber",
    "version": "14.0",

    "category": "Purchase Management",
    "post_init_hook": "post_init_hook",
    "depends": ["hr", "purchase_request"],
    "data": ["views/purchase_request_department_view.xml"],
    "license": "LGPL-3",
    "installable": True,
}
