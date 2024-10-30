from odoo import _, api, fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description =  """ 
                        Estate property type Model
                    """
    _order = "name,sequence desc"

    # SQL Constraints
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "A property type name must be unique"),
    ]

    # Fields
    name = fields.Char(string = "Property Type", required = True)
    sequence = fields.Integer(default = 1)
    offer_count = fields.Integer(compute = "_compute_offers_count")
    
    # Many2one and One2many fields
    property_ids = fields.One2many("estate.property", "property_type_id", string = "Property")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string = "Offers")

    # Private methods 
    @api.depends('offer_ids')
    def _compute_offers_count(self):
        for property in self:
            property.offer_count = len(property.offer_ids) 

    # Public methods
    def action_open_list_offers(self):
        return {
            "name" : _("Related offers"),
            "type" : "ir.actions.act_window",
            "view_mode" : "tree,form",
            "res_model" : "estate.property.offer",
            "target" : "current",
            "domain" : [("property_type_id", "=", self.id)],
            "context" : {"defaut_property_type_id" : self.id},
        }
    