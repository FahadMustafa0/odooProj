from odoo import models, fields, api


class inheritExam(models.Model):
     _inherit = "sale.order"

     x_sale_description = fields.Char(string='sale description')