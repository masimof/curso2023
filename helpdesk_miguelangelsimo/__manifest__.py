# Copyright <2023> <Miguel Angel Simó>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Miguel Angel Simó",
    "summary": "Gestiona incidencias",
    "version": "16.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    # "development_status": "Alpha|Beta|Production/Stable|Mature",
    "category": "helpdesk",
    "website": "https://github.com/masimof/curso2023",
    "author": "<Miguel Angel>, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    # "maintainers": ["your-github-login"],
    "license": "AGPL-3",
    # "application": False,
    "installable": True,
    # "preloadable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    #"external_dependencies": {
    #    "python": [],
    #    "bin": [],
    #},
    "depends": [
        "base",
    ],
    # this feature is only present for 11.0+
    #"excludes": [
    #    "module_name",
    #],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_action_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_tag_views.xml",
        "data/helpdesk_cron.xml",

        
    ],
 #   "demo": [
 #       "demo/assets.xml",
 #       "demo/res_partner_demo.xml",
 #   ],
 #   "qweb": [
 #       "static/src/xml/module_name.xml",
 #   ]
}