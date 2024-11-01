from odoo import _, api, fields, models
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
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute = "_compute_date_deadline", inverse = "_inverse_date_deadline")
    
    # Many2one and One2many fields
    partner_id = fields.Many2one("res.partner", required = True, string = "Partner")
    property_id = fields.Many2one("estate.property", required = True, string = "Property")
    property_type_id = fields.Many2one(related = "property_id.property_type_id", store = True)
   
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
    
    def action_refused(self):
        self.ensure_one()
        if self.property_id.selling_price == self.price :
            self.property_id.selling_price = 0.00
        self.status = "refused"

    @api.model
    def create(self, vals):
        # Get the property_id from vals
        property_id = vals.get('property_id')
        offer_price = vals.get('price')

        # Check if there are existing offers for the property with a higher amount
        existing_offers = self.search([
            ('property_id', '=', property_id),
            ('price', '>', offer_price)
        ])

        # existing_offers = property_id.offer_ids.filtered(lambda o: o.price > offer_price)
        # Fetch the property record if property_id is an integer
        # property_record = self.env['estate.property'].browse(property_id) if isinstance(property_id, int) else property_id
        # existing_offers = property_record.offer_ids.filtered(lambda o: o.price > offer_price)

        # print(f"f +++++++++++++++++ {property_id.offer_ids.filtered(lambda o: o.price > offer_price)}")
        if existing_offers:
            raise UserError(_('Cannot create this offer. The amount must be higher than existing offers.'))

        # Update the related property's state to 'Offer Received'
        property_record = self.env['estate.property'].browse(property_id)
        if property_record:
            property_record.write({'state': 'received'})
        
        # Call the super method to create the offer
        return super(PropertyOffer, self).create(vals)

    def extend_offer_deadline(self):
        activ_ids = self._context.get('active_ids', [])

        if activ_ids:
            offer_ids = self.env['estate.property.offer'].browse(activ_ids)
            for offer in offer_ids:
                offer.validity = 10