# Copyright <2021(S)> Felix Rojo>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Felix Rojo",
    "version": "14.0.1.0.0",
    "author": "Felix Rojo, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "data/delete_tag_cron.xml",
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_menu.xml",
        "views/helpdesk_view.xml",
        "wizards/create_ticket_view.xml",
        "views/helpdesk_tag_view.xml"
        
    ],

}