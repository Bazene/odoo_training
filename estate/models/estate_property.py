from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class RealEstate(models.Model):
    # Model name and description
    _name = "estate.property"
    _description =  """
                        Estate property model
                    """
    # Fields
    name = fields.Char(required=True)
    description = fields.Text() 
    postcode = fields.Char()

    def _default_date(self):
        return fields.Date.today() + relativedelta(months=3)

    date_availability = fields.Date(copy = False, default = _default_date)
    excepted_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("north", "North"), ("south", "South"), ("east", "East"), ("west", "West"),
    ])
    active = fields.Boolean(default = True)
    state = fields.Selection(
        [
            ("new", "New"), 
            ("received", "Offer Received"), 
            ("accepted", "Offer Accepted"), 
            ("sold", "Sold"), 
            ("canceled", "Canceled"),
        ], 
        required = True, 
        copy = False, 
        default = "new",
    )
    property_type_id = fields.Many2one("estate.property.type", string = "Property Type")
    buyer_id = fields.Many2one("res.partner", string = "Buyer", copy = False)
    salesperson_id = fields.Many2one('res.users', string = "Salesperson", default = lambda self: self.env.user)
    offer_ids = fields.One2many("estate.property.offer", "property_id", string = "Offers")
    tag_ids = fields.Many2many(
        'estate.property.tag',  # The related model (assuming this is your tag model)
        string='Tags'
    )
    total_area = fields.Integer(compute = "_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_price")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for property in self:
            property.best_price = max(property.offer_ids.mapped("price")) if property.offer_ids else 0

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area
