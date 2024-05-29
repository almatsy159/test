


fct = "3x^2+x/2"

fct1= "(3x+1)^A+(x/2)!A"

class Math_Function():

    def __init__(self,exp):

        self.exp = exp
        self.analyse_exp()

    def analyse_exp(self):

        self.map_nb={}
        self.map_lt={}
        self.map_ot={}
        self.map_of_map={1:self.map_nb,2:self.map_lt,3:self.map_ot}
        previous_c = ""
        for i in range(len(self.exp)) :
            x = self.exp[i]
            y = type(x)
            print(f"c = {x} de type : \n\t{y}")
            if isinstance(x,int):
                self.map_nb[i] = x
            elif not isinstance(x,int) or not isinstance(x,str):
                self.map_ot[i] = x

            else :
                #str
                map_lt[i] = x

            previous_c = x
        print(self.map_of_map)

Math_Function(fct)
