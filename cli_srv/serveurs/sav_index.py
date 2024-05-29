# coding: utf-8

import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme index.py at seveur/ </title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
    <p> <a href= "ressources/my_own_page.py">MY OWN PAGE Niveau -1 (.py) (in ressources) (dl) </a> </p>
    <p> <a href= "ressources/index.py">index Niveau -1 (.py) (in ressources) (dl)</a> </p>
    <!--<p> a href= "my_own_page_0.html" my own page 0 (.html) Niveau 0</a> (*blank)</p> -->
    <p> <a href="premiere_page_serveur.py"> my first page dedicated to a servor(.py) Niveau 0 </a>(*work)</p>
    <p> <a href="my_own_page.py">  my_own_page (.py) Niveau 0 </a>(*work)</p>
    <p> <a href= "ressources/script.py"> Vers script.py Niveau -1 </a> </p>
    <p> <a href= "script.py"> Vers script.py Niveau 0 </a> </p>
    <p> blank : mean code is incorrect (see cmd srv !) ; dl mean code is not interpreted but file is found (another level)</p>
        <p> Vers <a href= "http://www.wikipedia.org" target="_blank"> Wikipedia </a> </p>
</body>


</html>
"""

print(html)
