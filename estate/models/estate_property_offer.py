from odoo import api, fields, models
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = """
                    Offers made for real estates
                """
    # Fields
    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ], 
        copy = False,
        string ="Status"
    )
    partner_id = fields.Many2one("res.partner", required = True, string = "Partner")
    property_id = fields.Many2one("estate.property", required = True, string = "Property")
    property_type_id = fields.Many2one(related = "property_id.property_type_id", store = True)
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute = "_compute_date_deadline", inverse = "_inverse_date_deadline")

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for property in self:
            if property.create_date :
                property.date_deadline = property.create_date.date() + timedelta(days = property.validity)
            else : 
                property.date_deadline = fields.Date.today() + timedelta(days = property.validity)
            
    def _inverse_date_deadline(self):
        for property in self:
            if property.create_date and property.date_deadline:
                property.validity = (property.date_deadline - property.create_date.date()).days
