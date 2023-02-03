from odoo import models, fields, api


class AcademyTeachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()


