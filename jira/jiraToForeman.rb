# -*- utf-8 -*-
#!/usr/bin/ruby
require 'net/http'
require 'net/https'
require 'uri'
require 'cgi'
# if ruby = 1.8.7, need require 'rubygems' first for require 'json'
require 'rubygems'
require 'json'

def getJiraCookie
  uri = URI.parse("http://192.168.45.91:8080")
  http = Net::HTTP.new(uri.host, uri.port)
  req = Net::HTTP::Post.new("#{uri.path}/rest/auth/1/session")
  req.body = '{"username": "admin","password": "123456"}'
  req.content_type = 'application/json'
  response = http.request(req)
  return response.response['set-cookie']
end

def getJiraIssue
  cookie = getJiraCookie
  uri = URI.parse("http://192.168.45.91:8080")
  http = Net::HTTP.new(uri.host, uri.port)
  headers = {
    'Cookie' => cookie,
    'Content-Type' => 'application/json'
  }
  req = Net::HTTP::Post.new("#{uri.path}/rest/api/2/search", headers)
  #req.body = '{"jql": "labels in(\"NGINX\") AND status[name]=\"In Progress\"", "fields":["id","key","status", "customfield_10007"]}'
  req.body = '{"jql": "status[name]=\"In Progress\"", "fields":["id","key","status", "customfield_10007", "labels"]}'
  response = http.request(req)
  puts "issue: ",JSON.parse(response.body)
  return JSON.parse(response.body)
end

def getAgentName
  agents = {}
  issues = getJiraIssue()
  for issue in issues["issues"]
    temp = []
    temp << issue["fields"]["customfield_10007"]
    temp << issue["fields"]["labels"]
    agents[issue["key"]] = temp
  end
  return agents
end

def addClassesToForeman
  agents = getAgentName()
  for issueId in agents.keys()
    puts "add classes #{agents[issueId][1]} to #{agents[issueId][0]}"
    payload = { 'puppetclass_names' => agents[issueId][1], 'comment' => issueId}
    puts "payload: #{payload.to_json}----"
    agents[issueId][0].each do |agent|
      uri = URI.parse("http://192.168.45.11:3000")
      http = Net::HTTP.new(uri.host, uri.port)
      path = "/api/hosts/" + agent
      http.use_ssl = uri.scheme == 'https'
      http.verify_mode = OpenSSL::SSL::VERIFY_NONE
      req = Net::HTTP::Put.new("#{uri.path}#{path}")
      req.add_field('Accept', 'application/json,version=2')
      req.content_type = 'application/json'
      req.basic_auth "admin", "123456"
      req.body = payload.to_json
      response = http.request(req)
      res = JSON.parse(response.body)
      puts response.code
    end
  end
end

addClassesToForeman
