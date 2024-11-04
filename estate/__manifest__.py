{
    "name": "Real Estate",
    "author":"Serge",
    "version": "17.0.1.0",
    "category": 'Real Estate',
    "depends": ["base", "mail", "web", "website"],
    'license': 'LGPL-3',
    "installable":True,
    "application": True,
    'summary': 'Manage real estate properties',
    "description": """
        A module for managing real estate properties.
    """,
    "data": [
        # SECURITY
        "security/ir_rule.xml",
        "security/model_access.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",

        # VIEWS
        "views/res_users_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/estate_menu.xml",

        # DATA  FILES
        "data/mail_template.xml"
    ],
    "demo":[
        "demo/demo.xml"
    ],
    "assets" : {
        'web.assets_backend' : [
            'estate/static/src/js/my_custom_tag.js',
            'estate/static/src/xml/my_custom_template.xml',
        ],
    },
}
