# -*- utf-8 -*-
#!/usr/bin/ruby
# if ruby = 1.8.7, need require 'rubygems' first for require 'json'
require 'rubygems'
require 'json'
require 'net/http'
require 'net/https'
require 'uri'
require 'cgi'

uri = URI.parse("http://192.168.45.91:8080")
http = Net::HTTP.new(uri.host, uri.port)

def getJiraCookie
  uri = URI.parse("http://192.168.45.91:8080")
  http = Net::HTTP.new(uri.host, uri.port)
  req = Net::HTTP::Post.new("#{uri.path}/rest/auth/1/session")
  req.body = '{"username": "admin","password": "123456"}'
  req.content_type = 'application/json'
  response = http.request(req)
  return response.response['set-cookie']
end
def searchIssueStatus
  cookie = getJiraCookie
  uri = URI.parse("http://192.168.45.91:8080")
  http = Net::HTTP.new(uri.host, uri.port)
  headers = {
    'Cookie' => cookie,
    'Content-Type' => 'application/json'
  }
  req = Net::HTTP::Post.new("#{uri.path}/rest/api/2/search", headers)
  req.body = '{"jql": "labels in(\"STDLIB\") AND status[name]=\"In Progress\"", "fields":["id","key","status", "customfield_10007"]}'
  response = http.request(req)
  puts response
end

def changeIssueStatus
  cookie = getJiraCookie
  uri = URI.parse("http://192.168.45.91:8080")
  http = Net::HTTP.new(uri.host, uri.port)
  headers = {
    'Cookie' => cookie,
    'Content-Type' => 'application/json'
  }
  path = '/rest/api/2/issue/' + 'BAIS-1' + '/transitions?expand=transitions.fields'
  req = Net::HTTP::Post.new("#{uri.path}#{path}", headers)
  req.body = '{"transition":{"id":41}}'
  response = http.request(req)
  puts response
end



def getIssueIdFromForeman
  begin
    uri = URI.parse("https://foreman.example.com")
    http = Net::HTTP.new(uri.host, uri.port)
    path = "/api/hosts/agent.example.com"
    http.use_ssl = uri.scheme == 'https'
    #http.verify_mode = OpenSSL::SSL::VERIFY_NONE
    http.ca_file = "/var/lib/puppet/ssl/ca/ca_crt.pem"
    http.verify_mode = OpenSSL::SSL::VERIFY_PEER
    http.cert = OpenSSL::X509::Certificate.new(File.read("/var/lib/puppet/ssl/certs/foreman.example.com.pem"))
    http.key  = OpenSSL::PKey::RSA.new(File.read("/var/lib/puppet/ssl/private_keys/foreman.example.com.pem"), nil)
    req = Net::HTTP::Get.new("#{uri.path}#{path}")
    req.add_field('Accept', 'application/json,version=2')
    req.content_type = 'application/json'
    req.basic_auth "admin", "123456"
    response = http.request(req)
    res = JSON.parse(response.body)
    puts res["comment"]
  rescue Exception => e
    puts e
  end
end


getIssueIdFromForeman
