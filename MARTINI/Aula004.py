'''
lista = ['thiago',4,'pereira',3.14,True]
for i,j in enumerate(lista, start = -10):
    print(f'{i} é {j}')
    #i é o número dos i´ndices e j o conteúdo
ver = list(enumerate(lista))
print(ver)'''


'''
dict = {
    'nome': 'thiago',
            'a':326598415,
            'b':659898,
            'c':78945613,
            'sobrenome':'pereira'
}
soma = 0
for chave,conteudo in dict.items():
    if (type(conteudo)==int or type(conteudo) == float):
        soma = soma + conteudo
        print(f'{chave} é {conteudo}')
print(f'A soma dos valores do dict é {soma}')


'''
'''
dict = {
    'nome': 'thiago',
            'a':326598415,
            'b':659898,
            'c':78945613,
            'sobrenome':'pereira'
}
soma = 0
for chave,conteudo in dict.items():
    if (type(conteudo)==int or type(conteudo) == float):
        soma = soma + conteudo
        print(f'{chave} é {conteudo}')
print(f'A soma dos valores do dict é {soma}')
'''

'''
Revisão das variáveis primitivas:

str()
int()
float()
Bool()

Variáveis compostas:
tuplas(): são imultáveis; não pode adicionar elemento, nem remover
listas[]: são multáveis; 
dicionário{}: 

Métodos para as Listas:
.extend(): adiciona uma lista em outra
.isert(x,element): adiciona um elemento na posição x
.count(): conta o número de vezes que aparece o elemento
.pop(x): remove o elemento na posição x
.remove(x): remove o conteúdo x
no da lista [:]: faz a copia da lista

Métodos para os dicionários:
.pop(x): remove a chave x, ou seja, os dados referentes a esse campo
.keys(x): devolve as chaves do dict
.items(x): devolve os valores das chaves e valores do dict
.copy(): faz a copia dos dados digitados anteriormente e adiciona na lista


Obs.: matriz[l][c] = str(input(f'Digite um número para a posição [{l},{c}]: )
    faz com que apareça a posição da matriz no input***
'''

