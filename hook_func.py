from jira import JIRA


dicts = {"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
issue_key = dicts['pull_request']['head']['ref']

user = 'liads@at-bay.com'
apikey = 'ZS4eRIUhPIlDHareFyUs86AE'
server = 'https://cyberjack.atlassian.net/'
options = {'server': server}


def set_transition(issue_key_ticket):
    jira_server = {'server': server}
    jira = JIRA(options, basic_auth=(user, apikey))
    issue = jira.issue(issue_key)
    jira.transition_issue(issue, 11)
    jira.add_comment(issue, "shabat today")


print(set_transition(issue_key))
