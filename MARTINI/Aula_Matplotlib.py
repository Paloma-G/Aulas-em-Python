'''
Matpltlib possui um conjunto de submódulos
    matplotlib.pyplot: é uma interface baseada nos comandos de Matlab.
    matplotlib.image: uma interface para imagens.
    matplotlib.mlab: funções númericas escritas para compatibilidade com comandos Matlab com os
     mesmos nomes. Muito útil para processamento de sinais.

Tipos de Gráficos:

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.scatter(x,y) #gráfico de pontos
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.plot(x,y) #gráfico de linhas
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.bar(x,y) #gráfico de barras
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.barh(x,y) #gráfico de barras na horrizontal
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.pie(x,y) #gráfico de pizza
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20,21)
y = x**2-1
yy = x + 2
plt.plot(x,y,'ro',linewidth=2) # 'o'=bolinhas, 'r'=red, linewidth=espessura
plt.plot(x,y,'go--',linewidth=5) # 'o'=bolinhas, 'g'=green, linewidth=espessura, '--'=a ligação entre as bolinhas seja
# com traço.
plt.plot(x,y) #gráfico de linha
plt.title('Meu Gráfico') #Add título ao gráfico
plt.xlabel('eixo x') #Add o nomes dos eixo x
plt.ylabel('eixo y') #Add o nomes dos eixo y
plt.grid() # Add grade no gráfico para melhorar a vizualização
plt.xlim((-10,10)) #limita a vizualização do gráfico
plt.ylim((-50,100)) #limita a vizualização do gráfico
plt.show()

#Multiplos gráficos
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,1,100)
for i in range (15):
    plt.plot(x,x**i)
plt.show()


#Multiplos gráficos - Subplots
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20,21)
plt.subplot(2,2,1)
plt.plot(x,x)
plt.subplot(2,2,2)
plt.bar(x,x**2)
plt.subplot(2,2,4)
plt.scatter(x,x**3,linewidth=3)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1,1,100)
for i in range (1,7):
    plt.subplot(2,3,i)
    plt.plot(x,x**i)
    plt.title(f'Polinômio de {i} ordem')
plt.show()
'''


