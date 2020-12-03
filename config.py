debug=False #set to True if you want to have debugging output
proxy=False #set to True, if you want to use the proxy defiend in proxyip
proxies = { #set to the IPs of the proxy if you want to use it
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
}
vfy=True #check for proxy certificate

# relative path to the folder where the output is going to be written. Remember: it overwrites files with same name!
relative = True # Set to false, if you always want to go to a specific absolute path
path = ""
absolutepath = ""
output = True # set to false if you do not want to save the output

# Default parameters for the web calls
method = "GET"
redirect = False

#No change yet supported
file = ""
url = ""
header = {}
body = ""
tls = True
tls_port = 443
p_port = 80
hostname = 'https://github.com/JakeSamu/StandardWebFindings'
