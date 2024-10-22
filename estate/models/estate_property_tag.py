from odoo import fields, models

class EstateProperyTag(models.Model):
    _name = "estate.property.tag"
    _description = """
                        Estate property tag Model
                    """
    # Fields
    name = fields.Char(string = "Tag", required = True)
    property_ids = fields.Many2many(
        'estate.property',
        string = "Property"
    )
    color = fields.Integer()
    _order = "name"

    # SQL Constraints
    _sql_constraints = [
        ("unique_tag_name", "UNIQUE(name)", "A property tag name must be unique"),
    ]
