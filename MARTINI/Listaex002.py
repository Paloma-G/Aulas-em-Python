'''
Biblioteca math
Bem vamos voltar à biblioteca math. Essa biblioteca nos oferece algumas funções além da sqrt(), vou mostrar uma listinha abaixo:

math.sqrt(numero): Retorna a raíz quadrada do número.
math.cos(numero): Retorna o cosseno do número em radiano.
math.sin(numero): Retorna o seno do número em radiano.
math.tan(numero): Retorna a tangente do número em radiano.
math.radians(numero): Converte o angulo ‘numero’ de graus para radiano.
math.pi: Não é bem uma função, está mais para uma constante com o número pi (3.1415926535897931).
math.hypot(x, y): Retorna a hipotenusa dos números (catetos) fornecidos.
math.ceil: arredonda pra cima
math.floor: arredenda pra baixo
'''


'''
1) Crie uma rotina que solicite ao usuário dois lados de um
triângulo e ângulo , em graus, entre eles e retorna o
comprimento do terceiro lado. Use a lei dos cossenos.

a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
teta = float(input("Digite o ângulo teta do triângulo: "))

import math
tetar = math.radians(teta)
c = math.sqrt ((a*a)+(b*b)-(2*a*b*(math.cos(tetar))))

coss = math.cos(tetar)
print('O lado c do triângulo é {:.2f}, o cosseno é {:.2f}, teta em radiano é {:.2f}'.format(c,coss,tetar))

'''

'''
2) Crie uma rotina que solicite uma frase ao usuário e retorne
o número de caracteres na frase e o número de espaços.

s = str(input('Digite uma frase: '))
a= len(s) #conta o número de caracteres
b= s.count(' ') #conta o número de espaços vazios
l = a - b
print('letras {} e espaços vazios {}'.format(l,b))

'''

'''
3) No sistema SI, a vazão de um fluido é medida em metros
cúbicos por segundo (m3 /s). A medida do sistema inglês
de vazão, o pé cúbico por segundo (ft3/s) é equivalente
a 0.028 m 3 /s. Escreva uma rotina que pede ao usuário pela
vazão em metros cúbicos por segundo e converte essa vazão
para a unidade inglesa, exibindo o seguinte ao usuário:
Um fluxo de 15.2000 metros cúbicos por segundo
é equivalente a 542.8571 pés cúbicos por segundo

m = float(input('Qual é a vazão em metros cúbicos: '))
p = m / 0.028
print('Um fluxo de {:.3f} metros cúbicos por segundo \n é equivalente a {:.3f} pés cúbicos por segundo'.format(m,p))
'''

'''
4) Faça um programa que leia o nome completo de uma
pessoa e imprime somente o primeiro e o último nome
separadamente.

m = str(input('Qual é o seu nome completo? ')).strip() #tira os espaços
a = m.split() #separa as palavras
# len() informa quantas posições tem nome
print('Seu primeiro nome é {}'.format(a[0]), end='')
print('e o seu último sobrenome é {}'.format(a[len(a)-1])) 
'''

