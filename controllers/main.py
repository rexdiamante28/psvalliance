# -*- coding: utf-8 -*-
import base64

from odoo import SUPERUSER_ID
from odoo import http, _
from odoo.tools.translate import _
from odoo.http import request

from odoo.addons.website.models.website import slug

import logging
_logger = logging.getLogger(__name__)



class psvalliance(http.Controller):
    @http.route('/services', type='http', auth="public", website=True)
    def principal(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        return request.render("psvalliance.homepage", {})

    @http.route('/aboutus', type='http', auth="public", website=True)
    def aboutus(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        return request.render("psvalliance.homepage", {})



    @http.route('/page/signup', type='http', auth="public", website=True)
    def signup(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        return request.render("psvalliance.signup", {})


    #Ignore Mo Muna sir Unless I override mo yung Homepage
    #Overriding Homepage
    #@http.route('/page/homepage', type='http', auth="public", website=True)
    #def homepage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        #return request.render("psvalliance.homepage", {})


    @http.route('/page/contactus', type='http', auth="public", website=True)
    def contactus(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        return request.render("psvalliance.homepage", {})



    @http.route('/page/subscribe', type='http', auth="public", website=True)
    def submitdata(self, **kw):
        #Super ID which is ADMIN 1
        if not request.uid:
            request.uid = 1        

        #How to Call a Model in a Controller
        model_psvalliance_subscribers = http.request.env['psvalliance.subscribers'].sudo()


        #_logger.info('Name: ' + request.params['partner_name'])
        #_logger.info('Email: ' + request.params['partner_email'])
        #_logger.info('Company: ' + request.params['partner_company'])
        ##_logger.info('Contact Number: ' + request.params['partner_contactnumber'])
        #_logger.info('Message: ' + request.params['partner_message'])

        #Creation of New Record
        result = model_psvalliance_subscribers.create({
            'name' : request.params['name'],
            'email': request.params['email'],
            'company': request.params['company'],
            'contact_number': request.params['name'],
            'message': request.params['message']
        })




        return request.render("psvalliance.thankyou", {})        


    #Ignore Mo Muna sir Unless I override mo yung Homepage
    #Overriding Homepage
    #@http.route('/page/homepage', type='http', auth="public", website=True)
    #def homepage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("psvalliance.homepage", {})


    @http.route('/accountvendorlanding', type='http', auth="public", website=True)
    def vendorlandingpage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page

        #parnters = http.request.env['res.partners'].sudo()
        #partners = partners.search([['id', '=', '1']])

        #clients = http.request.env['psvalliance.clients'].sudo()
        #clients = clients.search([])

        #values = {
            #'clients': clients,
            #'curruser': partners
        #}


        partners = http.request.env['res.users'].sudo()
        partners = partners.search([['id', '=', http.request.uid]])


        values = {
            'partners': partners,
        }

        return request.render("psvalliance.accountvendorlanding", values)



    @http.route('/vendorpage', type='http', auth="public", website=True)
    def vendorpage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['customer', '=', True]])

        values = {
            'partners': partners,
        }

        return request.render("psvalliance.vendorhomepage", values)



    @http.route('/engagements', type='http', auth="public", website=True)
    def engagements(self, **kw):

        # copy this
        users = http.request.env['res.users'].sudo()
        users = users.search([['id', '=', http.request.uid]])

        partner_id = users[0].partner_id.id

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['id','=',partner_id]])

        partner_type = partners[0].psv_assigment # wrong spelling but kept it 'cause it raises an error if changed

        if request.session.uid and partner_type != 'VENDOR':
            return http.redirect_with_hash('/web')
        # up to this


        if request.httprequest.method == 'GET':
            engagements = http.request.env['psvalliance.engagements'].sudo()
            engagements = engagements.search([['psv_vendor','=', partner_id]])


            values = {
                'psv_engagements': engagements,
            }

            return request.render("psvalliance.engagements_template", values)


        if request.httprequest.method == 'POST':

            clients = http.request.env['psvalliance.clients'].sudo()
            clients = clients.search([['client_id','=', request.params['clientId']]])

            client_count = 0
            client_id = 1

            for psv_client in clients:
                client_count = client_count + 1
                client_id = psv_client.id


            if client_count < 1:
                engagements = http.request.env['psvalliance.engagements'].sudo()
                engagements = engagements.search([['psv_vendor','=', partner_id]])

                values = {
                    'error': 'Client does not exist. Please re-check and try again.',
                    'psv_engagements': engagements
                }

                return request.render("psvalliance.engagements_template", values)



            if client_count > 0:
                engagements = http.request.env['psvalliance.engagements'].sudo()

                result = engagements.create({
                    'psv_client': client_id,
                    'psv_vendor': partner_id
                })

                engagements = engagements.search([['psv_vendor','=', partner_id]])

                values = {
                    'success': 'Client engagement added',
                    'psv_engagements': engagements
                }

                return request.render("psvalliance.engagements_template", values)




    @http.route('/screeningpreview', type='http', auth="public", website=True)
    def screeningpreview(self, **kw):

        # copy this
        users = http.request.env['res.users'].sudo()
        users = users.search([['id', '=', http.request.uid]])

        partner_id = users[0].partner_id.id

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['id','=',partner_id]])

        partner_type = partners[0].psv_assigment # wrong spelling but kept it 'cause it raises an error if changed

        if request.session.uid and partner_type != 'VENDOR':
            return http.redirect_with_hash('/web')
        # up to this

        if request.httprequest.method == 'POST':

            _logger.info('SSSSSSSSSSSS' + request.params['surveylink'])

            values = {
                'surveylink': request.params['surveylink']
            }

            return request.render("psvalliance.screeningpreview", values)



    @http.route('/auditrequest', type='http', auth="public", website=True)
    def auditrequest(self, **kw):

        # copy this
        users = http.request.env['res.users'].sudo()
        users = users.search([['id', '=', http.request.uid]])

        partner_id = users[0].partner_id.id

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['id','=',partner_id]])

        partner_type = partners[0].psv_assigment # wrong spelling but kept it 'cause it raises an error if changed

        if request.session.uid and partner_type != 'VENDOR':
            return http.redirect_with_hash('/web')
        # up to this


        if request.httprequest.method == 'GET':
            audit_requests = http.request.env['psvalliance.auditrequests'].sudo()
            audit_requests = audit_requests.search([['psv_vendor','=', partner_id]])


            values = {
                'audit_requests': audit_requests,
            }

            return request.render("psvalliance.auditrequest", values)



        if request.httprequest.method == 'POST':

            clients = http.request.env['psvalliance.clients'].sudo()
            clients = clients.search([['client_id','=', request.params['clientId']]])

            client_count = 0
            client_id = 1

            for psv_client in clients:
                client_count = client_count + 1
                client_id = psv_client.id


            if client_count < 1:
                audit_requests = http.request.env['psvalliance.auditrequests'].sudo()
                audit_requests = audit_requests.search([['psv_vendor','=', partner_id]])

                values = {
                    'audit_requests': audit_requests,
                    'error': 'Client does not exist. Please re-check and try again.'
                }

                return request.render("psvalliance.auditrequest", values)



            if client_count > 0:

                auditrequests = http.request.env['psvalliance.auditrequests'].sudo()

                result = auditrequests.create({
                    'psv_client': client_id,
                    'psv_vendor': partner_id,
                    'date_requested': request.params['auditdate']
                })

                auditrequests = auditrequests.search([['psv_vendor','=', partner_id]])

                values = {
                    'audit_requests': auditrequests,
                    'success': 'Request sent. We will get back to you as soon as possible. Thank you.'
                }

                return request.render("psvalliance.auditrequest", values)




    @http.route('/paymentproof', type='http', auth="public", website=True)
    def paymentproof(self, **kw):

        # copy this
        users = http.request.env['res.users'].sudo()
        users = users.search([['id', '=', http.request.uid]])

        partner_id = users[0].partner_id.id

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['id','=',partner_id]])

        partner_type = partners[0].psv_assigment # wrong spelling but kept it 'cause it raises an error if changed

        if request.session.uid and partner_type != 'VENDOR':
            return http.redirect_with_hash('/web')
        # up to this

        if request.httprequest.method == 'POST':

            values = {
                'engagementid': request.params['engagementid']
            }

            return request.render("psvalliance.proof_of_payment", values)


        

    @http.route('/paymentproofupload', type='http', auth="public", website=True)
    def paymentproofupload(self, **kw):

        # copy this
        users = http.request.env['res.users'].sudo()
        users = users.search([['id', '=', http.request.uid]])

        partner_id = users[0].partner_id.id

        partners = http.request.env['res.partner'].sudo()
        partners = partners.search([['id','=',partner_id]])

        partner_type = partners[0].psv_assigment # wrong spelling but kept it 'cause it raises an error if changed

        if request.session.uid and partner_type != 'VENDOR':
            return http.redirect_with_hash('/web')
        # up to this

        if request.httprequest.method == 'POST':

            image = request.params['file_proof']
            image_read = base64.b64encode(image.read())


            _logger.info('iddddddddddddddddddddddddddd'+request.params['engagementid'])

            engagements = http.request.env['psvalliance.engagements'].sudo().search([['id', '=', request.params['engagementid']]]).write({
                'proof': image_read
            })

            
            values = {
                'engagementid': request.params['engagementid'],
                'success': 'Payment proof uploaded',
            }

            return request.render("psvalliance.proof_of_payment", values)






# vim :et:
