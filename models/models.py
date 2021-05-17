# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api,exceptions


class openacado(models.Model):
    _name = 'openacado.openacado'
    _description = 'openacado.openacado'

    name = fields.Char()
    description = fields.Char()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course', string="Sessions")

    # _sql_constraints =

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


class session(models.Model):
    _name = 'openacademy.session'
    _description = 'openacademy.session'

    name = fields.Char(string="Name")

    # defalut  value field
    start_date = fields.Date(string="Start_date", default=fields.Date.today)

    duration = fields.Float(string="Duration", digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course = fields.Many2one('openacado.openacado', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    # for graph view field
    # attendees_count = fields.Integer(
    #     string="Attendees count", compute='_get_attendees_count', store=True)

    # computed field
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    #    depends  used for dependencies
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    # Onchange method with warning
    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

        # Constraint to check instructor is not in session
        @api.constrains('instructor_id', 'attendee_ids')
        def _check_instructor_not_in_attendees(self):
            for r in self:
                if r.instructor_id and r.instructor_id in r.attendee_ids:
                    raise exceptions.ValidationError("A session's instructor can't be an attendee")
            # for graph view Method

        # @api.depends('attendee_ids')
        # def _get_attendees_count(self):
        #     for r in self:
        #         r.attendees_count = len(r.attendee_ids)



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
