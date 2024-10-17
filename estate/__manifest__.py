{
    "name": "Real Estate",
    "author":"Serge",
    "version": "17.0.1.0",
    "category": 'Real Estate',
    "depends": ["base"],
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
        "views/estate_property_views.xml",
    ],
    "demo":[
        "demo/demo.xml"
    ],
}
