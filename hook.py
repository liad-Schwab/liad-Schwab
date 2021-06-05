from jira import JIRA


dicts = {"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
ticket = dicts['pull_request']['head']['ref']

# credentials
user = 'liads@at-bay.com'
apikey = 'ZS4eRIUhPIlDHareFyUs86AE'
server = 'https://cyberjack.atlassian.net/'
options = {
 'server': server
}

# Authentication
jira = JIRA(options, basic_auth=(user, apikey))
#transition code
#TO_DO = 11, IN_PROGRESS = 21, DONE = 31
status_code =''
issue = jira.issue(ticket)
summary = issue.fields.summary
print('ticket: ', ticket, summary)
change_issue_status = jira.transition_issue(issue, 11)
jira.add_comment(issue, "Its thursday lets go home")
#transitions = jira.transitions(issue)
#jira.transitions(issue)
#print(transitions)
#jira.transition_issue(issue, 11,21)

def get_transition(issue_key):
    jira_server = {'server': config.jira_server}
    jira = JIRA(options=jira_server, basic_auth=(config.jira_user, config.jira_pass))
    issue = jira.issue(issue_key)
    transitions = jira.transitions(issue)
    for t in transitions:
        if t['name'] == config.jira_transition:
            return t['id']


def close_issue(issue, status):
    jira_server = {'server': config.jira_server}
    jira = JIRA(options=jira_server, basic_auth=(config.jira_user, config.jira_pass))
    jira.transition_issue(issue, status)






