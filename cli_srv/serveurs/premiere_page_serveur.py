import ressources.class_web2 as cw


page1=cw.Page()
#print(page1.objects)
#print(page1.content)

    # lecture en bd des param : type important pour BD
html=cw.Balise("html",{"lang":f"{lang}"},None,"",1,1,1,"html")
head=cw.Balise("head",{},html,"",1,1,1,"head")
meta=cw.Balise("meta",{"charset":f"{encoding}"},head,"",0)
title=cw.Balise("title",{},head,f"{page1.name}",1,0)
body=cw.Balise("body",{},html,"",1,1)
a1=cw.Balise("a",{"href":"index.py"},None,"link",1,0,0)
p1=cw.Balise("p",{},body,f"Hello my index is :{a1.body} here {a1.end} ;)",1,0,1)
h1=cw.Balise("h1",{},body,"Mon Titre 1",1,0,1)
strong = cw.Balise("strong",{},None,"usage de strong",1,0,0)
p2=cw.Balise("p",{},h1,f"{strong.body}{strong.end}",1,0,1)
h2_1=cw.Balise("h2",{},h1,"Mon Premier Titre 2",1,0,1)
mark = cw.Balise("mark",{},None,"usage de mark",1,0,0)
p3=cw.Balise("p",{},h2_1,f"{mark.body}{mark.end}",1,0,1)
h2_2=cw.Balise("h2",{},h1,"Mon Second Titre 2",1,0,1)
em = cw.Balise("em",{},None,"usage de em",1,0,0)
p4=cw.Balise("p",{},h2_2,f"{em.body}{em.end}",1,0,1)


page1.add_content(html.body)
print(page1.content)

with open("log_srv_premiere_page.txt","a+") as file:
    file.write("printing page content !")
