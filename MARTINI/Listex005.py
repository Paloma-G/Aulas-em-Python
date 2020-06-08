'''
4)


import numpy as np
from scipy.special import factorial
x = 2
exp = np.arange(2,100,2)
a = x**exp
b = factorial(exp)
termos = a/b
termos[::2] = -1*termos[::2] #do início até o fial pulando de 2 em dois e mult. por -1
cosvalue = termos.sum()+1
seno = np.sqrt(1-cosvalue**2)
print(seno)
print(cosvalue)
print(np.cos(x))
'''

