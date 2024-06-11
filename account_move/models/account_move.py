from odoo import models,fields


class AccountMove(models.Model):
    _inherit = 'account.move'

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # this field i want to add this field in add line in notebok in model account.move.line
    line_number = fields.Integer(string="Line Number", default=1)