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
class Index():
    def __init__(self):
        self.return_index()

    def return_index(self):
        href = "index.py"
        return href



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
"""
if __name__ == "__main__":
    # Test 1 : class Param()
    param1=Param("mon_nom_original","ma_valeur_originale")
    print(f"p1 : id_name : {param1.id}_{param1.name}\n\t my txt is : {param1.txt}")


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
            self.name = "Page"+str(self.page_id)
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
        self.content=f"<!doctype {self.doctype}\n\n"

    def add_content(self,content):
        self.content += content


if __name__ == "__main__":
    # Test 2 : Test Page()
    page1=Page()
    #print(page1.objects)
    #print(page1.content)
"""
# description type :

# type 0 : balise minimum
# type 1 : monoligne
# type 2 : monobalise

# type n : balise max
class Balise2():
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
    element_id = 0
    def __init__(self,value,param={},parent=None,content="",name=None):

        if name == None or name == "" :
            self.name= self.value + str(self.bal_id)
            self.print_name = 0
        else :
            self.name = name
        self.id = Element.element_id
        Element.element_id += 1
        self.type =  parent
        self.content = content
        self.param = param
        self.param["name"] = self.name
        self.param["id"] = self.id

        self.balise = Balise2(value)
        self.body = ""
        self.element_attr()

        self.final_content = f"{self.balise.beg}{self.type.body}{self.body}{self.content}{self.balise.end}"

    def element_attr(self):
        for i,j in self.param.items():
            self.body += f" {i}=\"{j}\""
        self.body += ">"

    def print_element(self):
        print(self.final_content)

e1=Element("card",{"posx":10,"posy":14,"class":"cards"},type_html,"Element_content","elt1")
e2=Element("card",{"posx":10,"posy":14,"class":"cards"},type_html2,"Element_content","elt2")
e1.print_element()
e2.print_element()

"""
class Balise_HREF():
    def __ini__(self,ref,lvl=0):
        self.ref = ref
        self.lvl = lvl
        self.prefix =""
        # cas du suffix jerecherche dans les sous dossier tree -L | grep ref
        self.sufix = ""

        if self.lvl > 0:
            if lvl == 0:
                self.prefix = "./"
            else :
                for i in range(self.lvl):
                    prefix += "../"
                # ...
        self.path = self.prefix + self.ref
        self.b = Balise()
#href1=Balise_Herf("index.py")
"""
class Balise():
    # need Param !
    bal_id = 0
    # gerer attr (type)  until content ?
    def __init__(self,value="p",param={},parent=None,content="",anti_balise = 1,retour_av=1,retour_ap=1,name=None,type=None,id=None,class_css=None,href=None):
        # a trier !!!
        self.href = href
        self.class_css = class_css
        self.value = value
        self.bal_id = Balise.bal_id
        Balise.bal_id += 1
        self.print_name=1
        if name == None or name == "" :
            self.name= self.value + str(self.bal_id)
            self.print_name = 0
        else :
            self.name = name
        self.contained_bal={self.name:{}}
        self.parent = parent
        if self.parent == None :
            self.lvl = 0
        else :
            self.lvl = self.parent.lvl + 1
            self.parent.add_child(self)
        self.type = type
        self.content=content
        self.param=param
        self.objects={}
        self.tabs=""
        for i in range(self.lvl):
            self.tabs += "\t"

        self.beg = f"{self.tabs}<{self.value}"
        self.body = self.beg
        if self.class_css != None:
            self.body += f"class ={self.class_css}"
        if self.href != None :
            self.body += f" href=\"{self.href}\""
        if id != None:
            self.body += f" id=\"{self.bal_id}\""
        if self.print_name == 1 :
            self.body += f" name=\"{self.name}\""
        for i,j in self.param.items() :
            name_tmp = i
            value_tmp = j
            p = Param(i,j)
            self.body += f" {i}=\"{j}\""
            self.objects[i] = p

        self.body += f">{self.content}"
        #self.body += ">"
        #self.body += self.content

        if retour_av == 1 :
            self.body += "\n"

        if anti_balise == 1 :
            if retour_av == 1:
                self.end = f"{self.tabs}</{value}>"
            else :
                self.end = f"</{value}>"
                #self.body += self.end
        else:
            self.end = ""
        if retour_ap == 1:
            self.end += "\n"

    def add_child(self,child):
        if isinstance(child,Balise):
            self.contained_bal[self.name][child.name] = child.contained_bal[child.name]
        else :
            self.contained_bal[self.name][child.name] = child


#### Can be method nd not class !!

class Html_list():
    def __init__(self,list1,parent=None,type="ul",list2=None):
        self.parent = parent
        self.type = type
        self.data_list = list1
        #self.len_data_lst = len(self.data_list)
        self.ref_list = list2
        if self.type =="ul" or self.type =="ol":
            self.html_list()
        elif self.type == "dl" and self.ref_list != None:
            self.def_list(self.data_list,self.ref_list)

    def html_list(self):
        self.dict_item={}
        self.balise=Balise(self.type,{},self.parent,"",1,1,1,"list")
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

    def add_lst_to_page(self,page):
        # bizare de passer par la page ...
        page.add_content(self.balise.body)
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
            page.add_content(content)
            compt += 1
        page.add_content(self.balise.end)



class NonOrd_list():
    def __init__(self,html_list,parent=None):
        self.parent = parent
        #print(html_list.obj_list)
        self.list= html_list.obj_list
        #self.list=[]

        self.dict_item={}
        self.balise_un=Balise("ul",{},self.parent,"",1,1,1,"un_list")
        compt =0
        for item in self.list :
            name = f"item_{compt}"
            b = Balise("li",{},self.parent,item,1,0,1,f"{name}")
            self.dict_item[name] = b
            compt+=1

class Ord_list(Html_list):
    def __init__(self,html_list,parent=None):
        self.parent = parent
        #print(html_list.obj_list)
        self.list= html_list.obj_list
        #self.list=[]

class Def_list():
    def __init__(self,html_list_def,html_list_term,parent=None):
        # meme taille de liste !
        self.parent = parent
        #print(html_list.obj_list)
        self.def_list= html_list_def.obj_list
        #self.list=[]

        self.dict_item={}
        self.balise_dl=Balise("dl",{},self.parent,"",1,1,1,"dl_list")
        compt = 0
        for item in self.def_list :
            # creation balise data term
            name1 = f"term_{compt}"
            b1 = Balise("dt",{},self.parent,item,1,0,1,f"{name1}")
            self.dict_item[name1] = b1
            # creation balise data def
            name2 = f"def_{compt}"
            b2 = Balise("dd",{},self.parent,item,1,0,1,f"{name2}")
            self.dict_item[name2] = b2

            compt+=1


"""
#Test 3 : Test Balise()

balise1 = Balise("div",params_test3,1,"paragraphe")
print(f"{balise1.body}\n\n{balise1.end}")
"""



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

html_lst1=Html_list(my_list,body)
html_lst1.add_lst_to_page(page1)
html_lst2=Html_list(my_list_of_term,body,"ol")
html_lst2.add_lst_to_page(page1)
html_lst3=Html_list(my_list,body,"dl",my_list_of_term)
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

#print("my_balise_id :",p4.id)


#print(html.contained_bal)
#print(head.contained_bal)
balises = [html.body,head.body,meta.body,title.body,title.end,head.end,body.body,p1.body,p1.end,h1.body,h1.end,
p2.body,p2.end,h2_1.body,h2_1.end,p3.body,p3.end,h2_2.body,h2_2.end,p4.body,p4.end,html.end]
#balises_end = [title.end,meta.end,head.end,html.end] #meta pas obligatoire


"""
#Test4 : Test List (ord)

my_list=["item1","item2","item3"]
my_html_list= Html_list(my_list)
# pas de parent !!! pas testé ! au dessus et dessous
my_ord_html_list = Ord_list(my_html_list)


page1.add_content(my_ord_html_list.balise_ol.body)
for i,j in my_ord_html_list.dict_item.items():
    content= "\t"+j.body + j .end
    page1.add_content(content)
page1.add_content(my_ord_html_list.balise_ol.end)



my_list_of_term=["i1","i2","i3"]
my_html_list_of_term=Html_list(my_list_of_term)
my_definition_list = Def_list(my_html_list,my_html_list_of_term)

# for a dict !!!

# liste de liste
sub_list1=["sub1","sub2"]

"""
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

"""
class Html(Page):
    def __init__(self,lang="fr",objects=None):

        super().__init__(self)
        self.lvl = super().lvl+1
        # name ? => Doc obj = dict !
        if obj == None:
            self.objects=[]
        else :
            self.objects = objects

        self.lang=lang
        self.head="<html"
        if lang != None :
            self.head += f" lang = \"{lang}\""
        self.headt= ">\n\t"

        self.tail="</html>"

class Meta():
    pass
class Head():
    def __init__(self):
        self.head_beg
"""
print(page1.content)
with open("./my_own_page.py","w+") as file :
    file.write(page1.content)
