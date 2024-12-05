from odoo import _, api, fields, models, tools
from datetime import date
class SchoolStudent(models.Model):
   
    _name = 'school.student'
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'Student'

    name = fields.Char(string="Nom de Famille", required=True, 
    track_visibility='onchange')
    birth_date= fields.Date(string='Date de naissance', default=date.today(),required=True, 
    track_visibility='onchange')
    photo = fields.Binary(string='Photo')
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est est ancien élève")
    sexe  = fields.Selection([
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
        ], 
    track_visibility='onchange')
    age = fields.Integer(string="Age", compute="_compute_age")
    note  = fields.Float(string="Note")
    class_id = fields.Many2one(
        'student.class',
        string='Classe',
        )
    cours_ids = fields.Many2many('school.cours', string="Cours")
    note_ids = fields.One2many('student.note', 'student_id')
    email = fields.Char(string='E-mail', 
    track_visibility='onchange')
    phone  = fields.Char(string='Téléphone', 
    track_visibility='onchange')

    state = fields.Selection([
        ('preinscription', 'Préinscription'),
        ('inscription','Inscription'),
        ('abandonne','Abandonné'),
        ('exclu','Exclu')
    ], default='preinscription')

    active = fields.Boolean(default=True)

    def compute_preinscription(self):
        for student in self:
            print('toto')
            student.state = 'preinscription'

    def compute_excul(self):
        for student in self:
            student.state = 'exclu'

    def compute_abandonne(self):
        for student in self:
            student.state = 'abandonne'

    def compute_inscription(self):
        for student in self:
            student.state = 'inscription'
    

    def _compute_age(self):
        for student in self:
            age=0
            if student.birth_date:
              today = date.today()
              birth_date = student.birth_date
              age = today.year - birth_date.year
            student.age = age
   