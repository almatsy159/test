
# coding: utf-8

import cgi
import ressources.class_web2

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <h1> MY TITLE </h1>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
        <div><p> <a href= "class_web3.py" >Classe web 3</a> </p></div>
    </form>
</body>
</html>
"""

print(html)
