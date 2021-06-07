from jira import JIRA
import datetime

user = 'liads@at-bay.com'
apikey = 'ZS4eRIUhPIlDHareFyUs86AE'
server = 'https://cyberjack.atlassian.net/'
options = {'server': server}
jira = JIRA(options, basic_auth=(user, apikey))

event_to_id = {
    'PR_initiated': 61,
    'branch_created': 71
}


def return_variables_from_github_hook(jira_ticket_id, git_event):
    dict_from_git = {
        "pull_request": {"head": {"ref": 'DEVOPSTEST-4'}},
        "ref_type": 'DEVOPSTEST-2',
        "action1": 'opened'
        }
    jira_ticket_id = dict_from_git['pull_request']['head']['ref']
    jira2_ticket_id = dict_from_git['ref_type']
    if dict_from_git['action1']:
        git_event = event_to_id["PR_initiated"]
    elif dict_from_git['ref_type']['DEVOPSTEST-2']:
        git_event = event_to_id["branch_created"]

    return jira_ticket_id, git_event


def set_transition(jira_ticket_id, git_event):
    issue = jira.issue(jira_ticket_id)
    jira.transition_issue(issue, git_event)


if __name__ == '__main__':
    jira_issue = {"pull_request": {"head": {"ref": 'DEVOPSTEST-4'}}}
    event_to_id = {'PR_initiated': 11, 'branch_created': 21}
    status_id_from_git_event = event_to_id["PR_initiated"]
    jira_issue, event_to_id = return_variables_from_github_hook(jira_issue, event_to_id)
    set_transition(jira_issue, event_to_id)
