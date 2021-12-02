from urllib.parse import urlencode
import json

import requests
from bottle import route, template, redirect, static_file, error, request, response, run


@route('/home')
def show_home():
    return template('home')

#routes to home page
@route('/zendesk_profile')
def make_request():
    if request.get_cookie('owat'):
        # Get user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        url = 'https://zccoestudents.zendesk.com/api/v2/users/me.json'
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get data with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            data = r.json()
            return template('details', data=data)
    else:
        # Kick off authorization flow
        parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'client_id': 'z',
            'scope': 'read write'}
        url = 'https://zccoestudents.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
        redirect(url)
        
@route('/showAllTickets')
def getTicketCounts():
    if request.get_cookie('owat'):
        # Get user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        url = 'https://zccoestudents.zendesk.com/api/v2/incremental/tickets/cursor.json?start_time=1532034771'
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get data with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            data = r.json()
            allTickets = []
            for ticket in data['tickets']:
                allTickets.append(ticket)
            return template('alltickets', data=allTickets)
    else:
        # Kick off authorization flow
        parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'client_id': 'z',
            'scope': 'read write'}
        url = 'https://zccoestudents.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
        redirect(url)

@route('/showTicket/<id>')
def showTicket(id):
    if request.get_cookie('owat'):
        # Get user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        url = 'https://zccoestudents.zendesk.com/api/v2/tickets/' + id + '.json'
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get data with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            data = r.json()
            return template('ticket', data=data['ticket'])
    else:
        # Kick off authorization flow
        parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'client_id': 'z',
            'scope': 'read write'}
        url = 'https://zccoestudents.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
        redirect(url)


@route('/handle_user_decision')
def handle_decision():
    if 'error' in request.query_string:
        return template('error', error_msg=request.query.error_description)
    else:
        # Get access token
        parameters = {
            'grant_type': 'authorization_code',
            'code': request.query.code,
            'client_id': 'z',
            'client_secret': '0c03cc225d42ef5a70799e59f4e64186ae3027a633f1d6def85cd59796297cce',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'scope': 'read'}
        payload = json.dumps(parameters)
        header = {'Content-Type': 'application/json'}
        url = 'https://zccoestudents.zendesk.com/oauth/tokens'
        r = requests.post(url, data=payload, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get access token with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            data = r.json()
            response.set_cookie('owat', data['access_token'])
            redirect('/home')

#redirects to home
@route('/')
def handle_root_url():
    redirect('/home')


@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')


@error(404)
def error404(error):
    return template('error', error_msg='404 error. Nothing to see here')


run(host='localhost', port=8080, debug=True)
