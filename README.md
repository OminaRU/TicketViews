# TicketViews

# Collaborators
Omina Elsheikh CS @ Baruch College '23 

# Contents
1. [Getting Started](#mylink) 

2. [Installation & Usage Instructions](#mylink2)

3. [Features]()

4. [Routing to all tickets]()

5. [Routing to individual tickets]()

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
 </p>