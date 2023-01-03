from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = ' Education Student'
    
    name = fields.Char(
        string='Name',
        required=True)
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Class', help="The Class of student")
    
    
    class_ids = fields.Many2many(
        comodel_name='education.class',
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes')

    ethnic_id = fields.Many2one('res.ethnic')
    ethnic_code = fields.Char(related='ethnic_id.code', store=True)
    
    ethnic_code2 = fields.Char(compute='_compute_ethnic_code2', store=True)
    enrollment_ids = fields.One2many('education.enrollment', 'student_id', readonly=True)

    enroll_class_ids = fields.Many2many(
        comodel_name='education.class',
        inverse_name='enroll_class_rel',
        string='Students',
        help="The students that belong to the class.",
        compute='_compute_enroll_class_ids')
    
    @api.depends('ethnic_id')
    def _compute_ethnic_code2(self):
        for r in self:
            r.ethnic_code2 = r.ethnic_id.code

    @api.constrains('enrollment_ids')
    def _compute_enroll_class_ids(self):
        for r in self:
            r.enroll_class_ids = enrollment_ids.student_ids

