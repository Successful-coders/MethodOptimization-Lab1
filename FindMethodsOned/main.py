#Task: write different methods of find min functions
#Variant 8, f(x)=(x-8)^2, x[-2,20]
import numpy as np
def f(x):
    return (x-8)**2
class Dichotomy:
    def x01(self,a,b):
        return (a+b-0.0001)/2

    def x02(self,a,b):
        return (a+b+0.0001)/2

    def DihotomyMethod(self,a,b):
        x1 = self.x01(a,b)
        x2 = self.x02(a, b)
        print (x1)
        print(x2)


a: float = -2
b: float = 20
dichotomy = Dichotomy()
dichotomy.DihotomyMethod(a,b)