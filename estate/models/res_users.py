from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    # Fields
    property_ids = fields.One2many(
        "estate.property", 
        "salesperson_id", 
        string = "Property",
        domain=[('state', 'in', ('new', 'received', 'accepted'))]  # Only show available properties
    )
