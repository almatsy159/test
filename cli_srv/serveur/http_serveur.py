#coding:utf-8
import http.server

def make_srv(p=80):
    PORT = p
    server_address = ("", PORT)

    # return html file from a link
    server = http.server.HTTPServer

    # execute
    handler = http.server.CGIHTTPRequestHandler

    handler.cgi_directories = ["/www/","/site1/"]

    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()


if __name__=="__main__":
    make_srv()
