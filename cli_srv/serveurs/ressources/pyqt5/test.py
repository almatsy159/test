class Test:
    
    def __init__(self):
        self.test1="osef"
        self.test2=2
        for i in range(2):
            name = "test"+str(i)
            self.name=name
            print(type(name)," ",name,self.name)


x = Test()
