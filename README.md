# TicketViews

# Collaborators
Omina Elsheikh CS @ Baruch College '23 

# Contents
1. [Getting Started](#mylink) 

2. [Installation & Usage Instructions](#mylink2)

3. [Features](#mylink3)

4. [Routing to all tickets](#mylink4)

5. [Routing to individual tickets](#mylink4)

# Getting Started
<p id="mylink"> Head over to the Zendesk website and create an account to start a 14 day free trial.
In creating your account, please use the prefix “zcc” in front of whichever
subdomain name you choose.
</p>

# Installation & Usage Instructions
1.  <p id="mylink2"> The first step is to create your test tickets. These will be used as a sample reference. 
Save the: <blockquote> <p>tickets.json</p></blockquote> file into your working directory.


 2.  Save the following: <blockquote> <p>curl https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json -v -u
{email_address}:{password} -X POST -d @tickets.json -H "Content-Type:
application/json</p></blockquote> curl command as you will need it to make the necessary POST request to your personal Zendesk account. 

Replace the email address and password placeholders with your personal account credentials. Paste the curl command into the terminal (assuming you are within the correct directory) to run the POST request. You will get a pretty lengthy JSON back with the list of tickets in your account and their corresponding details. You will have to parse through the data and format it so that it is easy to read. 
I used <a href="http://jsonprettyprint.net/">jsonprettyprint</a> to prettify the JSON to gain better insight into what i was looking at. 

# Setting Up 

3.  The "Ticket Viewer" web application builds off the python bottle framework.

# Why Bottle?
 Bottle is an out of the box WSGI micro-web framework for python. It's fast, lightweight, and easy to use with no dependencies exept for the Python STL(Standard Library). To get started, you must have python installed. Either the 2.7 or any 3 version will suffice. 
 Depending on which version you have, you will then pip install requests, and then bottle:
 ```
 pip3 install requests
 ```
 ```
 pip3 install bottle
 ```

# To set up your Bottle application

In a text editor, create a plain text file and save it as app.py in your project folder.

Create the following folders in the project folder:

* static/css
* views



Move your ticket_form.html file into the views folder.

Change the file's extension from ticket_form.html to ticket_form.tpl.

tpl stands for template. The framework renders templates into HTML to include in outgoing HTTP responses.

Move your form_styles.css file to its new home in the static/css folder.

Your project folder structure should now look like this:

```
1. /ticket_project
    2. app.py
    3. /static
    4.   /css
    5.        form_styles.css
    6./views
    7.   ticket_form.tpl
```
 </p>


 <p id="mylink3"> 
Routing: Requests to function-call mapping with support for clean and dynamic URLs.

Templates: Fast and pythonic built-in template engine and support for mako, jinja2 and cheetah templates.

Utilities: Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.

Server: Built-in HTTP development server and support for paste, bjoern, gae, cherrypy or any other WSGI capable HTTP server.

For more information on the Bottle Framework, visit: <a href="https://bottlepy.org/docs/dev/">Bottle Documentation</a>
 
 </p>

 # Routing to all tickets

 <p id="mylink4"> 
 
 See <blockquote> <p>oauth_app.py</p></blockquote> for code. 

Head over to your Zendesk Admin Center, then in the Oath clients tab, create a client name. This can be anything.

Next, take note of your unique client identifier, you will need this later.

Paste http://localhost:8080/handle_user_decision into Redirect URLs. Next, generate a secret key and keep it somewhere safe for use later. Hit save, and you are ready to go!

In your request route to your profile, 
paste 'https://your_subdomain.zendesk.com/api/v2/requests.json' in your url variable remembering to replace "your_subdomain" with your personal domain name. 

```
@route('/zendesk_profile')
def make_request():
    if request.get_cookie('owat'):
        # Get user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        
        url = ''
```

This route is making a request to your specific zendesk profile.

To make a request for all tickets, paste https://zccoestudents.zendesk.com/api/v2/incremental/tickets/cursor.json?start_time=1532034771' into the url variable below. 

```
@route('/showAllTickets')
def getTicketCounts():
    if request.get_cookie('owat'):
        # Getting user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        url = ''

```

The next route will make a request to each individual ticket, indexing the json data at 'id' to display the ticket id. 

```

@route('/showTicket/<id>')
def showTicket(id):
    if request.get_cookie('owat'):

```

Important!

your client_id is synonymous with your unique identifier. Place your unique identifier from your admin center there. 
 ..

 To run your app, type: 

 ```
 python3 APP_NAME.py 

 ```
 to start up the server. 

Your last major route will handle user decisions. Here is where you will paste your api key that you previously generated as your secret key. 

See the rest of the source code in the file. For further information, also see the  <a href= "https://developer.zendesk.com/documentation/ticketing/managing-tickets/building-a-custom-ticket-form-with-the-zendesk-api/">Zendesk Documentation</a> for a more in depth explanation about the source code, debugging, and testing. 
 </p>