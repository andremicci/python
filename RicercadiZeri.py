#!/usr/bin/env python
# coding: utf-8

# ### Ricerca di Zeri di una funzione 

# Vogliamo implementare un algoritmo di bisezione per la ricerca di zeri di una funzione in Python utilizzando un Notebook

# Fissiamo un intervallo in cui la funzione cambia segno, cioe\' il segno della funzione nei due estremi dell'intervallo ha segno opposto

# La funzione e\' $$f(x) =   x^{3}-1$$

# Importiamo i moduli necessari

# In[3]:


import matplotlib.pyplot as plt 
import numpy as np
import math


# Definiamo la funzione

# In[4]:


def func(x):
    return x**3 -1


# Grafichiamo $f(x)$. Creiamo un vettore di numpy di N=100 punti equidistanti tra x=0 e x=2

# In[6]:


x = np.linspace(0,2,100)


# Calcoliamo $y=f(x)$

# In[7]:


y = func(x)


# Creiamo un plot

# In[8]:


plt.plot(x,y)
plt.show()


# Ora dobbiamo implementare una funzione per la ricerca degli zeri. I parametri di questa funzione sono la funzione di cui voglio cercare lo zero, l\'estremo inferiore dell\'intervallo e l'estremo superiore e un valore di precisione con cui voglio conoscere il valore dello zero.

# In[9]:


def findZero(fun, emin, emax, tol):
    emed = (emin + emax)/2
    while ((emax-emin)>tol):
        fmed = fun(emed)
        fmin = fun(emin)
        if(fmed*fmin <=0):
            emax = emed
        else:
            emin = emed
        emed = (emin+emax)/2
    return emed;


# Ora chiamiamo la funzione per la ricerca di zeri passandogli la nostra funzione $f(x)$

# In[11]:


print(findZero(func, 0.,2., 0.001))


# In[ ]:




