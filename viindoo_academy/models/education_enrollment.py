from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EducationEnrollment(models.Model):
    _name = 'education.enrollment'
    _description = 'Education Enrollment'
    
    name = fields.Char(
        string='Ref.',
        required=True
        )

    class_id = fields.Many2one('education.class', string='Class')
    student_id = fields.Many2one('education.student', string='Student')
    date = fields.Date(help="The date on which the student enrolls")
    
    @api.constrains('class_id', 'student_id')
    def _constrains_class_student(self):
        for r in self:
            duplicate = self.search([
                ('class_id', '=', r.class_id.id),
                ('student_id', '=', r.student_id.id),
                ('class_id.state', '!=', 'draft')
                ])
            if duplicate:
                raise ValidationError(_("Student can't join in same class"))
            elif r.class_id.state != 'confirmed':
                raise ValidationError(_("Class must be confirmed before enroll student"))
