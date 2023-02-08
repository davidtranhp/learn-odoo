from odoo import models, fields, api


class AcademyTeachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    birthday = fields.Date(
        string="Date of birth"
        )
    age = fields.Integer(
        string='Age',
        compute='_compute_teacher_age'
        )
    biography = fields.Html()
    
    @api.depends('birthday')
    def _compute_teacher_age(self):
        today = fields.Date.today()
        for r in self:
            if r.birthday:
                r.age = today.year - r.birthday.year
            else:
                r.age = False

