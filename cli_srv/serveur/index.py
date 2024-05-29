# coding: utf-8

import cgi

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Le programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
    <p> <a href= "./serveur/my_own_page" > </p>
</body>
</html>
"""

print(html)
