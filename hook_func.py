from jira import JIRA

EVENTS = {
    "create_branch" : 11,
    "pr" : 21
}


user = 'liads@at-bay.com'
apikey = 'ZS4eRIUhPIlDHareFyUs86AE'
server = 'https://cyberjack.atlassian.net/'
options = {'server': server}

def return_variables_from_github_hook_event(event):
    issue_key = event['pull_request']['head']['ref']
    jirea_event = event[]

    return (jirea_event, issue_key )

def set_transition(issue_key_ev, event):
    jira_server = {'server': server}:
    jira = JIRA(options, basic_auth=(user, apikey))
    issue = jira.issue(issue_key_ev)
    jira.transition_issue(issue, event)
    jira.add_comment(issue, "shabat today")


if __name__ == '__main__':
    # DO HUKIM and play with them check if set trans works
    #event ={"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
    #event = {"": {"head": {"ref": 'DEVOPSTEST-1'}}}
    event = {"": {"head": {"ref": 'DEVOPSTEST-1'}}}
    git_objects =  return_variables_from_github_hook_event(event)
    set_transition(git_objects[0], git_objects[1])



#