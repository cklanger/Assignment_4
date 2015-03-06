"""
Assignment #4 problem 1
Computes the heat capacity as a function of the temperature T
for a 1000 cm^{3} piece of solide aluminum with number density
p=6.022e28 m{-3} and a Debye temp. of 428 K.
We use the trapezoidal rule to evaluate the integral with
N=1000 sample points. Note that the integrand is equal to zero
at x=0. We can rewrite the function as Cv=A*T^3*I, where I is the 
integral, and A=9V*p*kB/thetaD^3~0.0000954410422511699589 is a constant.
This program generates a plot of the heat capacity as a function of
temperature for T=5 K to T=500 K.
"""
from math import exp
from pylab import plot,show,xlabel,ylabel
def f(x):
    return x**4.0*exp(x)*(exp(x)-1)**(-2.0)
def cv(T):
    c=0.00009544104225116995893     # constant in front of integral        
    N=1000
    a=0.0
    b=428.0/T
    h=(b-a)/N
    s=0.5*f(b)
    for k in range(1,N):
        s+= f(a+k*h)
    return(h*s*c*T**3.0)
T=5.0
x=[]
y=[]
for k in range(1,496):
    x.append(T)
    y.append(cv(T))
    T+=1.0
print(T)
#print(x)
#print(y)
plot(x,y)
xlabel("Temperature (Kelvin)")
ylabel("Heat Capacity")
show()