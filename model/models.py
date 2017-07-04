# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subscribers(models.Model):
	_name = 'psvalliance.subscribers'

	name = fields.Char()
	email = fields.Char()
	company = fields.Char()
	contact_number = fields.Char(string='Contact Number')
	message = fields.Text()


class Clients(models.Model):
	_name = 'psvalliance.clients'
	_inherits = {'res.partner': 'partner_id', }

	id = fields.Integer('ID', readonly=True)
	client_id = fields.Char(string='Client ID')

	partner_id = fields.Many2one(
		'res.partner', 'Client', required=True, ondelete='cascade',
		help='Partner ID'
	)

	vendors = fields.One2many('res.partner', 'clients', string="Vendors")

	info = fields.Text(string='Extra info')
	active = fields.Boolean(
		'Active', default=True,
		help='If unchecked, it will allow you to hide contact without '
			 'removing it.'
	)


	@api.model
	def create(self, vals,):
		groups_proxy = self.env['res.groups']
		group_ids = groups_proxy.search([('name', '=', 'Client')])
		vals['groups_id'] = [(6, 0, group_ids)]
		return super(Clients, self).create(vals)



class Vendors(models.Model):
	#_name = 'psvalliance.vendors'
	#_inherits = {'res.partner': 'partner_id', }
	_inherit = 'res.partner'

	#id = fields.Integer('ID', readonly=True)

	clients = fields.Many2one('psvalliance.clients',
        ondelete='cascade', string="Client", required='True')

	company_name = fields.Char(string='Company Name')

	company_address = fields.Char(string='Company Address')
	contact_person = fields.Char(string='Contact Person')

	#partner_id = fields.Many2one(
	#	'res.partner', 'Vendor', required=True, ondelete='cascade',
	#	help='Partner ID'
	#)

	#info = fields.Text(string='Extra info')
	#active = fields.Boolean(
	#	'Active', default=True,
	#	help='If unchecked, it will allow you to hide contact without '
	#		 'removing it.'
	#)


	#@api.model
	#def create(self, vals,):
	#	groups_proxy = self.env['res.groups']
	#	group_ids = groups_proxy.search([('name', '=', 'Vendor')])
	#	vals['groups_id'] = [(6, 0, group_ids)]
	#	return super(Vendors, self).create(vals)