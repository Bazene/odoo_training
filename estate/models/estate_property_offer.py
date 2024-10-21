from odoo import fields, models

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

