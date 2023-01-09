from odoo import api, fields, models, _

class Student(models.Model):
    _name = 'school.student'
    _description = 'student'
    name = fields.Char('Student Name', reqired=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection('Gender', [('M','Male'), ('F','Female')])