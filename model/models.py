
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subscribers(models.Model):
	_name = 'psvalliance.subscribers'

	name = fields.Char()
	email = fields.Char()
	company = fields.Char()
	contact_number = fields.Char(string='Contact Number')
	message = fields.Text()
