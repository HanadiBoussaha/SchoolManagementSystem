from odoo import _, api, fields, models, tools
class SchoolCours(models.Model):
   
    _name = 'school.cours'
    _description = 'Cours'

    name = fields.Char(string="Nom du cours", required=True)