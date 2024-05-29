import sys
import os

doctype = "html"
lang = "fr"
encoding = "utf-8"
title = "My Title"
#link1 = "my_fist_link_to_css"
link_rel = "steelsheet"
link_href = "style.css"
script1_src = "script.js"

params_test3 = {"param1":"utf-8","param2":"osef_c'est_un_test"}

cwd = os.getcwd()
# commentaire pas gérés !!
def comment(str):
    return f"<!-- {str} -->"
# balise mal nommée : element , param : attribut et balise a l'interieur d'un element
#print(dir())
class Index():
    def __init__(self):
        self.return_index()

    def return_index(self):
        href = "index.py"
        return href
class List_of_Element():
    def __init__(self):
        self.elements=[]
        self.sequence=[]

    def create_sequence(self):
        seq = []
        for elt in self.elements:
            if isistance(elt,Element):
                #tmp = elt.method()
                tmp = f"{elt.balise.beg}{elt.type.param}{elt.param}>{elt.body}{elt.balise.end}"
                self.sequence.append(tmp)

    def add_element(self,element):
        self.elements.append(element)




class Param():
    id = 0
    def __init__(self,name,value):
        self.id = Param.id
        Param.id += 1
        self.txt = " " # un espace !
        self.name = name
        self.value = value
        self.txt += f"{self.name} = \"{self.value}\""
        self.param_dict={}
        self.param_dict[self.name] = self.value

class Balise():
    def __init__(self,name,balise=1,anti_balise=1):
        self.name = name
        self.beg = ""
        self.end = ""
        #if comment == None:
        if balise == 1:
            self.beg += f"<{self.name}"
        if anti_balise == 1:
            self.end += f"<\{self.name}>"


class Type_Element():
    id = 0
    def __init__(self,name,param={},content="",ret_beg=0,anti_balise=1,ret_end=0,ret_content=0):

        self.id = Type_Element.id
        Type_Element.id +=1

        self.content=content
        #self.type=type
        self.name = name
        self.param = param
        self.ret_end = ""
        if ret_end == 1:
            self.ret_end = "\n"
        if ret_beg == 1:
            self.ret_beg = "\n"

        """
        if self.value == 0 :
            self.anti_balise = 1
        """
        self.body = ""

        self.element_attr()
        """
        self.element_beg()

        if self.ret_beg == 1 :
            self.body += "\n"

        #self.body += self.content

        self.anti_balise = anti_balise

        if self.anti_balise == 1:

            self.end = ""
            if self.ret_content == 1 :
                self.end += "\n"

            self.element_end()
            if self.ret_end == 1 :
                self.end += "\n"

        """
    def element_attr(self):
        for i,j in self.param.items():
            self.body += f" {i}=\"{j}\""
    def element_beg(self):
        self.debut = f"<{self.name}{self.body}>"
    def element_end(self):
        self.fin = f"<\{self.name}>"

type_html=Type_Element("html",{"lang":"fr"},"content",1,1,1,1)
type_html2=Type_Element("html")

class Element():
    # miss certain points de Balise (v2)
    element_id = 0
    def __init__(self,value,param={},parent=None,type_elt=None,content="",name=None):

        self.id = Element.element_id
        Element.element_id += 1
        self.value = value

        if name == None or name == "" :
            self.name= self.value + str(self.id)
            self.print_name = 0
        else :
            self.name = name
        self.parent = parent
        if self.parent == None :
            self.lvl = 0

        else :
            self.lvl = self.parent.lvl + 1
            self.parent.add_child(self)

        self.type_elt=type_elt
        if  self.type_elt == None :
            self.type_elt = Type_Element(f"{self.name}_type")
        else :
            self.type_elt = type_elt
        self.contained = {self.name:{}}
        self.type_elt =  type_elt
        self.content = content
        self.param = param

        self.param["name"] = self.name
        self.param["id"] = self.id

        self.balise = Balise(value)
        self.body = ""
        self.element_attr()
        print(f"type:{self.type_elt}")
        self.final_content = ""
        # f"{self.balise.beg}{self.type_elt.body}{self.body}{self.content}{self.balise.end}"

    def element_attr(self):
        for i,j in self.param.items():
            self.body += f" {i}=\"{j}\""
        self.body += ">"

    def print_element(self):
        print(self.final_content)

    def add_child(self,child):
        if isinstance(child,Element):
            self.contained[self.name][child.name] = child.contained[child.name]
        else :
            self.contained[self.name][child.name] = child

js1={"posx":10,"posy":14,"class":"cards"}
e1=Element("card",js1,None,type_html,"Element_content","elt1")
e2=Element("card",js1,None,type_html2,"Element_content","elt2")
e1.print_element()
e2.print_element()

class Html_list():
    # meme class vue de l'element !
    # liste est un element (ol,ul) qui contient une multitude d'element (li)
    def __init__(self,list1,parent=None,type="ul",list2=None):
        self.parent = parent
        # if parent == None !
        self.type = type
        self.data_list = list1
        self.content = ""
        #self.len_data_lst = len(self.data_list)
        self.ref_list = list2
        if self.type =="ul" or self.type =="ol":
            self.html_list()

        elif self.type == "dl" and self.ref_list != None:
            self.def_list(self.data_list,self.ref_list)
        self.create_content()

    def html_list(self):
        self.dict_item={}
        self.balise=Element(self.type,{},self.parent,"","list")
        compt =0
        for item in self.data_list :
            name = f"item_{compt}"
            b = Balise("li",{},self.parent,item,1,0,1,f"{name}")
            self.dict_item[name] = b
            compt+=1

    def def_list(self,def_list,term_list):
        #print(html_list.obj_list)
        #self.list=[]
        self.dict_item={}
        self.balise=Balise("dl",{},self.parent,"",1,1,1,"dl_list")
        compt = 0
        for item in def_list :
            # creation balise data term
            name1 = f"term_{compt}"
            b1 = Balise("dt",{},self.parent,item,1,0,1,name1)
            self.dict_item[name1] = b1
            # creation balise data def
            name2 = f"def_{compt}"
            b2 = Balise("dd",{},self.parent,term_list[compt],1,0,1,name2)
            self.dict_item[name2] = b2
            compt+=1

    def create_content(self):
        res = self.balise.body
        compt=0
        for i,j in self.dict_item.items():
            if self.type =="dl":
                if compt % 2 == 1:
                    var ="\t\t"
                else :
                    var="\t"
            else :
                var ="\t"
            content= var+j.body + j .end
            res+=content
            compt += 1
        res+=self.balise.end
        self.content = res


class Page():
    page_id = 0
    def __init__(self,name=None,obj=None,doctype=None):
        if doctype == None :
            self.doctype = "html"
        else :
            self.doctype = doctype
        self.page_id = Page.page_id
        Page.page_id += 1
        if name == None :
            self.name = f"Page{str(self.page_id)}"
        else :
            self.name = name
        self.lvl=0
        self.objects=[]
        #self.doctype = doctype
        if obj != None:
            self.objects.append(obj)
            #obj.
        self.doc_beg=""
        self.doc_end=""
        self.content=f"<!doctype {self.doctype}>\n\n"

    def add_content(self,content):
        self.content += content


page1=Page()
#print(page1.objects)
#print(page1.content)

# lecture en bd des param : type important pour BD

html=Balise("html",{"lang":f"{lang}"},None,"",1,1,1,"html")
head=Balise("head",{},html,"",1,1,1,"head")
meta=Balise("meta",{"charset":f"{encoding}"},head,"",0)
title=Balise("title",{},head,f"{page1.name}",1,0)
body=Balise("body",{},html,"",1,1)
"""
my_list=["item1","item2","item3"]
my_list_of_term=["i1","i2","i3"]

html_lst1=Html_list(my_list)
html_lst1.add_lst_to_page(page1)
html_lst2=Html_list(my_list_of_term,None,"ol")
html_lst2.add_lst_to_page(page1)
html_lst3=Html_list(my_list,None,"dl",my_list_of_term)
html_lst3.add_lst_to_page(page1)
"""

a1=Balise("a",{"href":"index.py"},None,"link",1,0,0)
p1=Balise("p",{},body,f"Hello my index is :{a1.body} here {a1.end} ;)",1,0,1)
h1=Balise("h1",{},body,"Mon Titre 1",1,0,1)
strong = Balise("strong",{},None,"usage de strong",1,0,0)
p2=Balise("p",{},h1,f"{strong.body}{strong.end}",1,0,1)
h2_1=Balise("h2",{},h1,"Mon Premier Titre 2",1,0,1)
mark = Balise("mark",{},None,"usage de mark",1,0,0)
p3=Balise("p",{},h2_1,f"{mark.body}{mark.end}",1,0,1)
h2_2=Balise("h2",{},h1,"Mon Second Titre 2",1,0,1)
em = Balise("em",{},None,"usage de em",1,0,0)
p4=Balise("p",{},h2_2,f"{em.body}{em.end}",1,0,1)


#print(html.contained_bal)
#print(head.contained_bal)
balises = [html.body,head.body,meta.body,title.body,title.end,head.end,body.body,p1.body,p1.end,h1.body,h1.end,
p2.body,p2.end,h2_1.body,h2_1.end,p3.body,p3.end,h2_2.body,h2_2.end,p4.body,p4.end,html.end]
#balises_end = [title.end,meta.end,head.end,html.end] #meta pas obligatoire


def add_to_page(page,balises):
    for balise in balises :
        page.add_content(balise)

add_to_page(page1,balises)
#add_to_page(page1,balises_end)



html0= f"""<!doctype {doctype}>
<html lang="{lang}">
<head>
  <meta charset="{encoding}">
  <title>Titre de la page</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
  ...
  <!-- Le reste du contenu -->
  ...
</body>
</html>
"""

with open("./my_own_page.py","wa+") as file :
    file.write(page1.content)

print(page1.content)
