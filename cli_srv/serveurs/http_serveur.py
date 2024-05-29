import http.server
print(http.server)

PORT = 80
server_address = ("", PORT)

# recoit des requetes
server = http.server.HTTPServer

# gere l'execution du script python
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
