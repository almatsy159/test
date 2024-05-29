class Parent():
    def __init__(self,name):
        self.name=name
        self.id=self


class Child1():
    def __init__(self,parent,name):
        self.parent=parent
        self.name=name
        self.id=self

class Child2(Parent):
    def __init__(self,parent,name):
        self.parent=super().__init__(parent)
        self.name=name
        self.id=id


p1=Parent("p1")
print(p1)

c1=Child1(p1,"c1")
print(c1," : ",c1.__dict__,";",c1.__repr__())

c2=Child2(p1,"c2")
print(c2," : ",c2.__dict__,";",c2.__repr__())
