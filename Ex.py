from http.server import HTTPServer, BaseHTTPRequestHandler

htmlcontent = '''
<!doctype html>
<html>
<head>
<title> Sample </title>
</head>
<body>
<font color="blue" face="Lucida Handwriting" size="120">
            <h1 align="center"> <b> List of protocol in TCP/IP Model</b></h1>
        </font>
        <font color="red">
        <h2>
            Application Layer - HTTP, FTP, DNS, Telnet & SSH <br>
            Transport Layer - TCP & UDP <br>
            Network Layer - IPV4/IPV6 <br>
        </h2>
        </font>
</body>
</html>
'''
class ServerResponse(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,ServerResponse)
httpd.serve_forever()