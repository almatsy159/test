# coding: utf-8

import cgi
import cgitb

dsp = 0
ld = "/log"
cgitb.enable(display=dsp, logdir=ld)

#print(dir(cgi))
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <title>Mon programme index.py at client_server/md/ </title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
    <p>
    <p> <a href= "HTML_from_MD.py"> HTML from MD </a>Niveau 0 (.html)  \n </p>
    <p> <a href= "Py_from_HTML.py"> Py from HTML </a>Niveau 0 (.py)  \n </p>

</body>
<footer>
<p> my foot: <a href="mailto:localhost@hostname">mail to localhost@hostname.com</p>
</footer>

</html>
"""

print(html)
