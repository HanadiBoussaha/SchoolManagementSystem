from odoo import _, api, fields, models, tools

class StudentNote(models.Model):
   
    _name = 'student.note'
    _description = 'Note de l\'élève'
    _rec_name = 'cours_id'

    cours_id = fields.Many2one(
        'school.cours',
        string='Cours',
        )

    exam_note = fields.Float(string="Note d'examen")

    student_id = fields.Many2one(
        'school.student',
        string='Student',
        )
