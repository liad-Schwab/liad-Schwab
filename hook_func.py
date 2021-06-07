from typing import Dict

from jira import JIRA


date_object = datetime.date.today()
print(date_object)


GIT_HOOK_EVENTS = {
    "branch_created": x,
    "PR_initiated": y,
    "PR_approved": z,
    "PR_merged_to_master": w
}


def return_variables_from_github_hook(json):
    pr_dict = {"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
    create_dict = {"ref_type": 'test_brunch01'}
    jira_id = pr_dict['pull_request']['head']['ref']

    return github_event_type, jira_id


def set_transition(jira_issue_key_, status):
    user = 'liads@at-bay.com'
    apikey = 'ZS4eRIUhPIlDHareFyUs86AE'
    server = 'https://cyberjack.atlassian.net/'
    options = {'server': server}
    jira = JIRA(options, basic_auth=(user, apikey))
    issue = jira.issue(jira_issue_key_)
    jira.transition_issue(issue, status)
    #jira.add_comment(issue, date_object )


if __name__ == '__main__':
    #event ={"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
    #new_branch_name = {"ref_type" : 'test_brunch01'}
    issue_jira = {"pull_request": {"head": {"ref": 'DEVOPSTEST-1'}}}
    github_event_type, jira_issue_id = return_variables_from_github_hook_event(str(git_event), issue_jira)
    set_transition(git_objects[0], git_objects[1])



#