from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EducationCourse(models.Model):
    _name = 'education.course'
    _description = 'Education Enrollment'
    
    name = fields.Char(string='Course Name.', required=True)
    
    class_ids = fields.One2many(
        comodel_name='education.class',
        inverse_name='course_id',
        string="Class")
    
    student_ids = fields.Many2many(
        comodel_name='education.student',
        string="Class")

    description = fields.Html(string='Description')
