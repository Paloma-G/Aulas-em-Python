'''lanche = ('a','b','g') #tuplas; não pode mudar
print(lanche[2])

lanches = ['a','b','g'] #listas; pode mudar
print(lanches[2])
lanches[2] = 't'
print(lanches[2])

lanches.append('h') #add no fial a lista
print(lanches[3])

lanches.insert(0,'f') #add em qq posição
print(lanches)

del lanches[3] #remove a 3 posição
lanches.pop(3) #remove a 3 posição
#lanches.remove('t')
print(lanches) #remove o 3 item
#se o item não estiver na lista ela não é rmoida
if 'b' in lanches:
    lanches.remove('b')
print(lanches)

valores = list(range(4,11)) #faz uma lista
print(valores)
valores2 = [8,4,9,3,1]
valores2.sort() #ordena a lista
print(valores2)
valores2.sort(reverse=True) #ordena de forma decrescente
print(valores2)
l = len(valores2)
print(l)'''

'''
ex.1
num = [2,5,9,1]
num[2]= 3
num.append(7)
print(num)
num.sort(reverse=True)
num.insert(2,0)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 5')

'''


'''
ex.2
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...',end='')

for c,v in enumerate(valores):
    print(f'\n Na posição {c} encontrei o valor {v}')
print(f'\n Cheguei ao final da lista')
'''

'''
ex.3
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print(f'Cheguei ao final!')
'''

'''
ex.3

a = [2,3,4,7]
#b = a  faz a ligação entre uma lista e outra
b = a[:] #esfz essa ligação, fazendo uma copia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

'''

