# coding: utf-8
import cgi
print("Content-type: text/html; charset=utf-8\n")

html='''<!DOCTYPE HTML>
<html lang="fr">
<head>
<title>HTML_from_MD</title>
</head>
<body><h1>My_First_MarkDown_Doc</h1>
<h1></h1>
<hr />
<p>|col1|col2|col3|</p>
<hr />
<p>|l1c1|l1c2|l1c3|
|l2c1|l2c2|l2c3|</p>
<hr />
<blockquote>
<p>a
b
c
d</p>
</blockquote>
<p>string</p></body>
</html>'''

print(html)
