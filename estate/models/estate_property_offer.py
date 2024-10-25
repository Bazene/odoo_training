from odoo import api, fields, models
from datetime import timedelta
from odoo.exceptions import UserError

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = """
                    Offers made for real estates
                """
    _order = "price desc"

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
    
    # SQL Constraints
    _sql_constraints = [
        ("check_offer_price", "CHECK(price > 0)", "An offer price must be strictly positive"),
    ]

    # Private methods
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
    
    # Public methods
    # methods for accepted and refuse offers buttons
    def action_accept(self):  
        self.ensure_one()  # Ensure the recordset contains only one record
        if "accepted" in self.property_id.offer_ids.mapped('status'):
            raise UserError("This property has already an offer")
        
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
    
    def action_Refused(self):
        self.ensure_one()
        if self.property_id.selling_price == self.price :
            self.property_id.selling_price = 0.00
        self.status = "refused"
