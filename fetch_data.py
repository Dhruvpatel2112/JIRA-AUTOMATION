from jira.client import JIRA
import json
import configs
options = {'server': 'http://10.0.1.78'}
jira = JIRA(options, basic_auth=(configs.userName, configs.passWord))
###fetching jira projects
projects = jira.projects()
dic_project={}
file_json_rsponse=open("./json_response.txt","w")
###listing jira projects
for project in projects:
    print(project.name)
###fetching issuess of projects and create json dump
for project in projects:
    issues_in_proj = jira.search_issues('project={}'.format(project))
    # print(issues_in_proj[0].raw) prining issue object as json format
    for issue in issues_in_proj:
        print(issue.raw)
        file_json_rsponse.write(json.dumps(issue.raw))
    break    
    
