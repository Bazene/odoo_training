from odoo import fields,models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description =  """ 
                        Estate property type Model
                    """
    # Fields
    name = fields.Char(string = "Property Type", required = True)

     # SQL Constraints
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "A property type name must be unique"),
    ]
