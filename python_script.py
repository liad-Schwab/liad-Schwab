import random
import json
from jira import JIRA
import request, Response, jsonify


app = Flask(__name__)

#Consider flow control Flask 
@app.route('/webhook', methods=['POST'])
def respond():
    #print (request.json)
    #print (request.data)
    data = request.get_json()
    name = data.get('name', '')
    change_isuue_status = jira.transition_issue(issue, 21)
    return Response(status=200)
    



@app.route('/', methods=['GET']) 
def index():
    return render_template("index.html") 


user = 'moxocim146@troikos.com'
apikey = 'Fzv6UcNnutzNOFDrD3dB0A4E'
server = 'https://shwebs84.atlassian.net/'
options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )
ticket = 'GIT-1'
issue = jira.issue(ticket)
summary = issue.fields.summary
print('ticket: ', ticket, summary)
#jira.add_comment(issue, "iron DOM rools")
#transitions = jira.transitions(issue)
jira.transitions(issue)
print(transitions)
#jira.transition_issue(issue, 11,21)
