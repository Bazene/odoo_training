from odoo import api, fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description =  """ 
                        Estate property type Model
                    """
    _order = "name,sequence desc"

    # Fields
    name = fields.Char(string = "Property Type", required = True)
    sequence = fields.Integer(default = 1)
    offer_count = fields.Integer(compute = "_compute_offers_count")
    
    # Many2one and One2many fields
    property_ids = fields.One2many("estate.property", "property_type_id", string = "Property")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string = "Offers")

    # SQL Constraints
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "A property type name must be unique"),
    ]

    # Private methods 
    @api.depends('offer_ids')
    def _compute_offers_count(self):
        for offer in self:
            offer.offer_count = len(offer.offer_ids) 

    # Public methods
