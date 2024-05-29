# coding: utf-8

import cgi

#print(dir(cgi))
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

    <p> <a href=""#1"> Vers id = 1 </a> </p>
    <p> <a href= "ressources/my_own_page.py">MY OWN PAGE </a>Niveau -1 (.py) (in ressources) (dl) \n </p>
    <p> <a href= "ressources/index.html">index  (dl)</a>Niveau -1 (.html) (in ressources) \n</p>
    <p> <a href= "ressources/my_own_page_0.html"> my own page 0 (.html) </a> Niveau -1 (in ressource)(*wrok !!!)</p>

    <p> <a href="premiere_page_serveur.py"> my first page dedicated to a servor(.py) </a>Niveau 0 (*work)</p>
    <p> <a href="my_own_page.py">  my_own_page (.py)  </a>Niveau 0(*work)</p>
    <p> <a href= "script.py"> Vers script.py  </a>Niveau 0 </p>
    <p> <a href= "class_web2.py"> class web 2  </a>Niveau 0 </p>

    <p> <a href= "ressources/script.py"> Vers script.py Niveau -1 </a> </p>

    <p> blank : mean code is incorrect (see cmd srv !) ; dl mean code is not interpreted but file is found (another level)</p>

    <p id=1> Vers <a href= "http://www.wikipedia.org" target="_blank"> Wikipedia </a> </p>

    <p>Dl file : <a href= "log_srv.txt"> Myfile "log_srv.txt </a>. </p>
</body>
<footer>
<p> my foot: <a href="mailto:localhost@hostname">mail to localhost@hostname.com</p>
</footer>

</html>
"""

print(html)
