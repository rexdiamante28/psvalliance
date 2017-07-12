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

	name = fields.Char(string='Name', required='True')

	client_id = fields.Char(string='Client ID')

	vendors = fields.One2many('res.partner', 'clients', string="Vendors")

	info = fields.Text(string='Extra info')
	active = fields.Boolean(
		'Active', default=True,
		help='If unchecked, it will allow you to hide contact without '
			 'removing it.'
	)

	phone = fields.Char(string='Phone')
	mobile = fields.Char(string='Mobile Number')
	fax = fields.Char(string='Fax')
	email = fields.Char(string='Email')
	address = fields.Text()

	image = fields.Binary()

	survey_link1 = fields.Char(string='Initial Survey Link')
	survey_link2 = fields.Char(string='Follow Up Survey Link')




class Vendors(models.Model):
	#_name = 'psvalliance.vendors'
	#_inherits = {'res.partner': 'partner_id', }
	_inherit = 'res.partner'

	#id = fields.Integer('ID', readonly=True)

	clients = fields.Many2one('psvalliance.clients',
        ondelete='cascade', string="Client")

	company_name = fields.Char(string='Company Name')

	company_address = fields.Char(string='Company Address')
	contact_person = fields.Char(string='Contact Person')

	c_id = fields.Char(string='Client ID')

	#clientID = fields.Char(string='Client ID')

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

	#@api.model
    #def create(self, vals,):
   	#	cur_clients = self.env['psvalliance.clients']
    #	cur_client = cur_clients.search([['client_id','='self.c_id]])
    #	self.clients = cur_client.client_id
    #	return super(Vendors,self).create(vals0