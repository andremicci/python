import matplotlib as plt
import numpy as np
import math 


def a(sigma,f,x):
    return (x**2/sigma**4)*f -f/sigma**2

def soleq(n1,n2,sigma):
    #creo f (copia di x)
    f=np.array(x)
    j=sign(n2-n1)
    
    f[0]=0
    f[1]=1.0e-4
    

    for i in range(n1+2*j,n2+1,1):
        #verlet position
        f[i]=2*f[i-j]-f[i-2*j]+h*h*a(sigma,f[i-j],x[i-j])
#
##main code
sigma=1
n=10000
x=np.linspace(-5,5,n)
h=x[1]-x[2]

f=soleq(0,9999,1)
plt.plot()