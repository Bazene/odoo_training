from odoo import fields,models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description =  """ 
                        Estate property type Model
                    """
    _order = "name,sequence desc"

    # Fields
    name = fields.Char(string = "Property Type", required = True)
    property_ids = fields.One2many("estate.property", "property_type_id", string = "Property")
    sequence = fields.Integer(default = 1)

     # SQL Constraints
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "A property type name must be unique"),
    ]
