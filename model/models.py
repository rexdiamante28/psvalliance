# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clients(models.Model):
	_name = 'psvalliance.clients'

	name = fields.Char(string='Name', required='True')

	client_id = fields.Char(string='Client ID')

	vendors = fields.One2many('psvalliance.engagements', 'psv_client', string="Vendors")

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



class Engagements(models.Model):
	_name = 'psvalliance.engagements'

	name = fields.Char()
	psv_client = fields.Many2one('psvalliance.clients', ondelete = 'cascade', string='Client')
	psv_vendor = fields.Many2one('res.partner', ondelete = 'cascade', string='Vendor')

	survey_link1 = fields.Char(string='Initial Survey Link')
	survey_link2 = fields.Char(string='Follow Up Survey Link')

	paid = fields.Boolean()
	proof = fields.Binary()

	remark1 = fields.Selection([('n/a', 'N/A'), ('for_review', 'For Review'), ('with_risk', 'With Risk'), ('without_risk','Without Risk')], default='n/a', string='Initial Screening Remark')
	remark2 = fields.Selection([('n/a', 'N/A'), ('for_review', 'For Review'), ('with_risk', 'With Risk'), ('without_risk','Without Risk')], default='n/a', string='Initial Screening Remark')

	@api.model
	def create(self, values):
		client_id = values.get('psv_client')
		cid = self.env['psvalliance.clients'].search([('id','=',client_id)], limit=1)
		values['survey_link1'] = cid.survey_link1
		values['survey_link2'] = cid.survey_link2

		result = super(Engagements, self).create(values)

		return result



class auditReuests(models.Model):
	_name = 'psvalliance.auditrequests'

	psv_client = fields.Many2one('psvalliance.clients', ondelete = 'cascade', string='Client')
	psv_vendor = fields.Many2one('res.partner', ondelete = 'cascade', string='Vendor')
	date_requested = fields.Date(string='Requested Audit date')

	status = fields.Selection([('for_confirmation','For Confirmation'),('scheduled','Scheduled'), ('done', 'Done')], default='for_confirmation')
	remarks = fields.Char()

	

class Vendors(models.Model):
	_inherit = 'res.partner'

	psv_assigment = fields.Char(string = 'PSV User Type') # wrong spelling but kept it 'cause it raises an error if changed
	company_name = fields.Char(string='Company Name')

	company_address = fields.Char(string='Company Address')
	contact_person = fields.Char(string='Contact Person')

	
	#@api.model
	#def create(self, values):
	#	client_id = values.get('clients')
	#	cid = self.env['psvalliance.clients'].search([('client_id','=',client_id)], limit=1)
	#	values['cid'] = cid.id

	#	result = super(Vendors, self).create(values)

	#	return result

	# @api.model
 #    def create(self, values):
 #        cid = self.env['psvalliance.clients'].search([('client_id', '=','clients')], limit=1)
 #        values['cid'] = cid.id

 #        result = super(PrimerRepair, self).create(values)

 #        return result


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