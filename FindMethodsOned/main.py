#Task: write different methods of find min functions
#Variant 8, f(x)=(x-8)^2, x[-2,20]
import numpy as np
def f(x):
    return (x-2)**2
eps = 1e-7
delta = 1e-9
class Dichotomy:
    def x01(self,a,b):
        return (a+b-delta)/2

    def x02(self,a,b):
        return (a+b+delta)/2

    def DihotomyMethod(self,a,b):
        i = 0
        pred = 1
        x1 = self.x01(a, b)
        x2 = self.x02(a, b)
        print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b-a, "\t", pred / b-a,
              "\t")
        i = i + 1
        while(abs(b-a) > eps):

            x1 = self.x01(a, b)
            x2 = self.x02(a, b)
            pred = b-a
            if(f(x1)<f(x2)):
                b = x2
            else:
                a = x1
            print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b - a, "\t", pred / b - a,
                  "\t")
            i = i + 1

class GoldenRatio:
    def x01(self,a,b):
        return a+0.381966011*(b-a)

    def x02(self,a,b):
        return a+0.618003399*(b-a)
    def GoldenRatioMethod(self, a,b):
        i = 0
        pred = 1
        x1 = self.x01(a, b)
        x2 = self.x02(a, b)
        print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b - a, "\t", pred / b - a,
              "\t")
        i=i+1
        while(abs(b-a) > eps):
            x1 = self.x01(a, b)
            x2 = self.x02(a, b)
            pred = b-a
            if(f(x1)<f(x2)):
                b = x2
                x2 = x1
            else:
                a = x1
                x1 = x2
            # print("i:", i)
            # print("a", a)
            # print("b", b)
            # print("b-a", b - a)
            # print("x1:", x1)
            # print("x2:", x2)
            # print("f(x1):", f(x1))
            # print("f(x2):", f(x2))
            print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b - a, "\t", pred / b - a,
                  "\t")
            i = i + 1

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
        comp = d/eps
        pred = 1
        while (comp > self.Fib(n+2)):
            n = n+1
        x1 = self.x01(a, b, n)
        x2 = self.x02(a, b, n)

        print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b - a, "\t", pred / b - a,
              "\t")
        for j in range (n-1):
            pred = b-a
            if(f(x1)<f(x2)):
                b = x2
                x2 = x1
                x1 = self.x01(a,b,n)
            else:
                a = x1
                x1 = x2
                x2 = self.x02(a,b,n)
            i=i+1
            print(i, "\t", x1, "\t", x2, "\t", f(x1), "\t", f(x2), "\t", a, "\t", b, "\t", b - a, "\t", pred / b - a,
                  "\t")



def FindMinInterv(x0,d):
    xpred=0
    if f(xpred) > f(xpred + d):
        k = 1
        xnext = xpred+d
        h = d
    else:
        if f(xpred) > f(xpred - d):
            xnext = xpred - d
            h = -d
    h = h*2
    print(k, "\t", xpred,"\t", xnext, "\t", f(xpred), "\t", f(xnext))
    while(f(xpred)>f(xnext)):
        k = k + 1
        xpred = xnext
        h = h * 2
        xnext = xpred + h
        print(k, "\t", xpred,"\t", xnext, "\t", f(xpred), "\t", f(xnext))



a: float = -2
b: float = 20
# print("Dichotomy method:")
# dichotomy = Dichotomy()
# dichotomy.DihotomyMethod(a,b)

# goldenRatio = GoldenRatio()
# goldenRatio.GoldenRatioMethod(a,b)

# fibonachi = Fibonachi()
# fibonachi.FibonachiMethod(a,b)
x0 = float(input("Enter x0 "))
d = float(input("Enter delta "))
FindMinInterv(x0, delta)