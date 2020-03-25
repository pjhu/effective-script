# butch sending
# curl -s --user 'api:xxxx' \
#     https://api.mailgun.net/v3/xxxx/messages \
#         -F from='Digital <digital@xxxx>' \
#         -F to=xxxx@xxx \
#         -F to=xxx@xxx \
#         -F subject='Digital test' \
#         -F text='Digital test' \
#         -F attachment=@/Users/twcn/work/pjhu/effective-script/mailgun/test-test.xlsx

# mail list
curl -s --user 'api:dbfb0bceccb06847145208350cbb7b34-9525e19d-4e60a53a' \
    https://api.mailgun.net/v3/mg.costajapan.com/messages \
        -F from='Info <info@costajapan.com>' \
        -F to='costafortwtest@gmail.com' \
        -F to='jiachen.zhang@costa.it' \
        -F subject='Digital test' \
        -F text='Digital test'

# curl -s --user 'api:xxxxx' \
# 	https://api.mailgun.net/v3/xxx/messages \
# 	-F from='postmaster@xxx' \
# 	-F to=wechat@xxx \
# 	-F subject='Hello' \
# 	-F text='Testing some Mailgun awesomeness!'
