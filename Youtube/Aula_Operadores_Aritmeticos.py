'''
+ Adição
- Subtração
/ Divisão
* Multiplicação
** Potência ou pow(número,elevado) ou **(1/2) raiz quadrada
% Resto da divisão
// Divisão inteira -> Módulo
== Testar se algo no primeiro membro é igual ao do segundo membro
= Atribuição

Ordem de procedência: 1º parênteses, 2º Potência, 3º (*; /; //; %), 4º Adição e subtração
'''

''' 
#Escreve o nome normal
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

#Escreve o nome com um espaço de 20 caracteres
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

#Escreve o nome com um espaço de 20 caracteres alinhado a direita
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))

#Escreve o nome com um espaço de 20 caracteres alinhado a esquerda
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))

#Escreve o nome com um espaço de 20 caracteres centralizado
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))

#Escreve o nome com um espaço de 20 caracteres centralizado com igual em volta do nome
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

'''

n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {},\n o produto é {} \ne a divisão é {:.3f}'.format(s,m,d), end=' ')
# O termo end=' ' cola a linha de cima com a e baixo
# O \n pula a linha
print('Divisão inteira {} e potência {}'.format(di,e))