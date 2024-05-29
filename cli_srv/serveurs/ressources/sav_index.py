"""
<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
</body>
</html>
"""
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme from {/.../client_serveur/servers/index.py} 20/04/2022 </title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
    <p> <a href= "my_own_page.py" > NIVEAU 0 vers "my_own_page.py"  </a></p>
    href= "../index.py" >NIVEAU +1 vers "index" </a> </p>
    <p> <a href= "script.py"> Vers script.py Niveau 0 </a> </p>
</body>
</html>
"""

print(html)
