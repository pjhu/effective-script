# -*- utf-8 -*-
import requests
import json


def getJiraCookie():
    print("Get Jira Cookie")
    url = "http://192.168.45.91:8080/rest/auth/1/session"
    payload = { "username": "admin", "password": "123456"}
    _headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=_headers)
    print(r.status_code)
    return r.cookies


def getJiraIssue():
    url = 'http://192.168.45.91:8080/rest/api/2/search'
    payload = {"jql": "labels in(\"STDLIB\") AND status[name]=\"In Progress\"", "fields":["id","key","status", "customfield_10007"]}
    _headers = {'content-type': 'application/json'}
    r = requests.post(url, cookies=getJiraCookie(), data=json.dumps(payload), headers=_headers)
    print(r.json())
    return r.json()


def getAgentName():
    agents = {}
    issues = getJiraIssue()
    for issue in issues["issues"]:
        agents[issue["key"]] = issue["fields"]["customfield_10007"]
    return agents


def addClassesToForeman():
    agents = getAgentName()
    for issueId in agents.keys():
        print(issueId, agents[issueId])
        payload = { "puppetclass_names": ["stdlib","stdlib::stages"], "comment":issueId }
        for agent in agents[issueId]:
            url = "http://controller.scaleworks.net/api/hosts/" + agent
            _headers = {"content-type": "application/json", "Accept": "version=2,application/json"}
            _auth = ("admin", "123456")
            r = requests.put(url, auth=_auth, data=json.dumps(payload), headers=_headers, verify=False)
            print(r.status_code)

if __name__ == "__main__":
    print("start...")
    addClassesToForeman()
    print("Done")
