{
    "name": "Real Estate",
    "author":"Serge",
    "version": "17.0.1.0",
    "category": 'Real Estate',
    "depends": ["base","mail"],
    'license': 'LGPL-3',
    "installable":True,
    "application": True,
    'summary': 'Manage real estate properties',
    "description": """
        A module for managing real estate properties.
    """,
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",

        # VIEWS
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/estate_menu.xml",

        # REPORT
        "report/report_template.xml",
        "report/property_report.xml",
    ],
    "demo":[
        "demo/demo.xml"
    ],
}
