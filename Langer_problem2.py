"""
Assignment 4 problem 2
Computes the integral of e^(t^2)
from t=0 to t=x. First we calculate this
integral, E(x), for x=0 to x=3 in 0.1 steps.
Then we plot E(x) for a range of x values.
We use the trapezoidal rule to perform the quadrature,
as the integration is fast and reliable for 2000 slices,
whereas using Simpson's rule the program is much slower.
"""
from math import exp
from pylab import plot,show,xlabel,ylabel
def f(t):
    return exp(t*t)
def E(x):
    h=(x-a)/N
    s=0.5*f(a)+0.5*f(x)
    for k in range(1,N):
        s+=f(a+k*h)
    return h*s
r=[]
y=[]
N=2000
a=0.0
x=0.01
while x<3.0:        # change this to x<M to plot E(x) from x=0 to x=M
    r.append(x)
    y.append(E(x))
    x+=0.01
# print(y)     uncomment this line to print the array of E(x) for steps of x
plot(r,y)
xlabel("x")
ylabel("E(x)")
show()
