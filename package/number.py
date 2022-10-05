class number:
    
    def check_even_odd(self,x):
        self.x=x
        if x%2 == 0:
           print(format(self.x),"is an even number")

        else:
           print(format(self.x),"is an odd number")

    def check_positive_negative(self,y):
        self.y=y
        if y > 0:
           print(format(self.y),"is a positive number")

        else:
           print(format(self.y),"is an negative number")



n=number()
n.check_even_odd(110)  
n.check_positive_negative(234)

