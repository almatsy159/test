class Test():
    x=10
    y=8
    print("je m'execute dans tout les cas")
    def __init(self):
        y=5
        print(y)
        self.x=Test.x
        self.y=y
        print(self.y)
print("out x: ",Test.x)
print("out y: ",Test.y)

test1=Test()

