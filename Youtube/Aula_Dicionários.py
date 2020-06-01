'''
Teoria

tuplas ()
Listas []
Dicionários {}

'''
dados = dict()
dados = {'nome':'Pedro','idade':25}
print(dados)
dados['sexo'] = 'M' #add elementos
print(dados)
del dados['idade']
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())

for k , v in dados.items():
    print(f'O {k} é {v}')

#pode juntar o dicionário em uma lista



'''
ex.1

pessoas = {'nome':'Paloma','sexo': 'F','idade':23}
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
'''

'''
ex.2

pessoas = {'nome':'Paloma','sexo': 'F','idade':23}
#pessoas['nome'] = 'Pedro'    pode alterar o nome
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k}={v}')
'''

'''
ex.3

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[1]['uf'])
'''

'''
ex.4

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str (input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copia o elemento anterior
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(v,end=' ')
        print( )


'''