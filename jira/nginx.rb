# -*- utf-8 -*-
#!/usr/bin/ruby
# if ruby = 1.8.7, need require 'rubygems' first for require 'json'
require 'rubygems'
require 'json'
require 'net/http'
require 'net/https'
require 'uri'
require 'cgi'

class NginxConfig

  UPSTREAM = 'stubapp'

  def getProdIp
    begin
      uri = URI.parse('https://172.31.61.81')
      http = Net::HTTP.new(uri.host, uri.port)
      path = '/api/hosts?search=facts.kfcjboss_app=true+and+facts.is_in_place=true+params.kfcjboss_role=prod'
      http.use_ssl = uri.scheme == 'https'
      http.verify_mode = OpenSSL::SSL::VERIFY_NONE
      req = Net::HTTP::Get.new("#{uri.path}#{path}")
      req.add_field('Accept', 'application/json,version=2')
      req.content_type = 'application/json'
      req.basic_auth 'admin', '123456'
      response = http.request(req)
      hosts = JSON.parse(response.body)
      hosts['results'].map{|host| host['ip']}
    rescue Exception => e
      puts e
    end
  end

  def getPilotIp
    begin
      uri = URI.parse('https://172.31.61.81')
      http = Net::HTTP.new(uri.host, uri.port)
      path = '/api/hosts?search=facts.kfcjboss_app=true+and+facts.is_in_place=true+params.kfcjboss_role=pilot'
      http.use_ssl = uri.scheme == 'https'
      http.verify_mode = OpenSSL::SSL::VERIFY_NONE
      req = Net::HTTP::Get.new("#{uri.path}#{path}")
      req.add_field('Accept', 'application/json,version=2')
      req.content_type = 'application/json'
      req.basic_auth 'admin', '123456'
      response = http.request(req)
      hosts = JSON.parse(response.body)
      hosts['results'].map{|host| host['ip']}
    rescue Exception => e
      puts e
    end
  end

  def prod_upstream
    prod_servers = getProdIp.map {|host| "  server #{host}:18080;" }.join('\n')
"
upstream prod{
  #{prod_servers}
}
"
  end

  def pilot_upstream
    pilot_servers = getPilotIp.map {|host| "  server #{host};" }.join('\n')
"
upstream pilot{
  #{pilot_servers}
}
"
  end


  def ips_pilot_condition(ips)
    ip_reg=ips.gsub(";","\n").gsub(",","\n").split("\n").join("|")
    "if ($remote_addr ~ \"^(#{ip_reg})\") {
      set $web_backend pilot;
    }"
  end

  def percent_pilot_condition(percent)
    percent_reg=(0..(percent.gsub("%","").to_i/10-1)).map(&:to_s).join("|")
    "if ($remote_addr ~ \".*(#{percent_reg})$\") {
      set $web_backend pilot;
    }"
  end


  def config(ips,percent)
ret = <<EOF
#{prod_upstream}
#{pilot_upstream}


server {
  listen 80;
  set $web_backend prod;
  #{ips_pilot_condition(ips)}
  #{percent_pilot_condition(percent)}

  location / {
    proxy_pass http://$web_backend;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header Host $http_host;
    proxy_set_header X-NginX-Proxy true;

    #include proxy.conf;
  }
}
EOF
  end
end
puts NginxConfig.new.config(ARGV[0],ARGV[1])

=begin
upstream prod{
    server 172.31.158.205:18080;
}

upstream pilot{
    server 172.31.158.91;
}

server {
  listen 80;
  set $web_backend prod;
  if ($remote_addr ~ "^(172.31.61.86|172.31.61.82|172.31.158)") {
    set $web_backend pilot;
  }
  if ($remote_addr ~ ".*(0|1)$") {
    set $web_backend pilot;
  }

  location / {
    proxy_pass http://$web_backend;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header Host $http_host;
    proxy_set_header X-NginX-Proxy true;

    #include proxy.conf;
  }
}
=end
