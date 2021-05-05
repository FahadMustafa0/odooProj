from odoo import models,fields

class minimalModel(models.Model):
    _name='first_model'
    _description = "this is my first model"
    name=fields.Char(requirments=True)

class Course(models.Model):
    _name = "openacademy.course"
    name=fields.Char(String='title',required=True)
    description = fields.Text()
