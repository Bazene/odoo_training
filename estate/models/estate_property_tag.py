from odoo import fields, models

class EstateProperyTag(models.Model):
    _name = "estate.property.tag"
    _description = """
                        Estate property tag Model
                    """
    # Fields
    name = fields.Char(string = "Tag", required = True)
