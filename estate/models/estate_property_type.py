from odoo import fields,models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description =  """ 
                        Estate property type Model
                    """
    # Fields
    name = fields.Char(required = True)
