'''
Teoria
pessoas = [['Pedro',25],['Maria',19],['João',32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

'''

'''
ex.1
teste = list()
teste.append('Paloma')
teste.append(23)
galera = list()
galera.append(teste[:]) # faz uma copia do teste
print(teste)
teste[0] = 'Cristina'
teste[1] = 45
galera.append(teste [:]) 
print(galera)


'''


'''
ex.2
galera = [['João',19],['Ana',22],['Ricardo',4],['Gustavo',33]]
print(galera)
print(galera[0])
print(galera[0][0])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

'''

'''
ex.3

galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')
'''
