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
        i=1
        while(abs(b-a)> 0.001):
            print ("i:",i)
            print("a",a)
            print("b",b)
            print("b-a",b-a)
            x1 = self.x01(a, b)
            print ("x1:",x1)
            x2 = self.x02(a, b)
            print("x2:",x2)
            print("f(x1):", f(x1))
            print("f(x2):", f(x2))
            if(f(x1)<f(x2)):
                b = x2
            else:
                a=x1
            i=i+1
            print("\n")

class GoldenRatio:
    def x01(self,a,b):
        return a+0.381966011*(b-a)

    def x02(self,a,b):
        return a+0.618003399*(b-a)
    def GoldenRatioMethod(self, a,b):
        i = 1
        while(abs(b-a)>0.001):
            print("i:", i)
            print("a", a)
            print("b", b)
            print("b-a", b - a)
            x1 = self.x01(a, b)
            x2 = self.x02(a, b)
            print("x1:", x1)
            print("x2:", x2)
            print("f(x1):", f(x1))
            print("f(x2):", f(x2))
            if(f(x1)<f(x2)):
                b = x2
                x2 = x1
            else:
                a = x1
                x1 = x2
            i = i + 1
            print("\n")

class Fibonachi:
    def x01(self,a,b,n):
        return a + (self.Fib(n+1) / self.Fib(n+3))*(b-a)

    def x02(self,a,b,n):
        return a + (self.Fib(n+2) / self.Fib(n+3))*(b-a)

    def Fib(selfself, n):
        if n < 3:
            return 1
        return selfself.Fib(n - 1) + selfself.Fib(n - 2)

    def FibonachiMethod(self, a,b):
        i = 0
        n=1
        d= (b-a)
        comp = d/0.001
        while (comp > self.Fib(n+2)):
            n = n+1
        x1 = self.x01(a, b, n)
        x2 = self.x02(a, b, n)

        for j in range (n-1):
            if(f(x1)<f(x2)):
                b = x2
                x2 = x1
                x1 = self.x01(a,b,n)
            else:
                a = x1
                x1 = x2
                x2 = self.x02(a,b,n)
            print("a", a)
            print("b",b)
            print("b-a",b-a)
            print("x1",x1)
            print("x2",x2)
            print("f(x1)", f(x1))
            print("f(x2)", f(x2))
            print("\n")





a: float = -2
b: float = 20
print("Dichotomy method:")
dichotomy = Dichotomy()
dichotomy.DihotomyMethod(a,b)

#goldenRatio = GoldenRatio()
#goldenRatio.GoldenRatioMethod(a,b)

#fibonachi = Fibonachi()
#fibonachi.FibonachiMethod(a,b)

