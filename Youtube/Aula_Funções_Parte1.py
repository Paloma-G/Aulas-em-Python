'''
#Criação de um comando novo (personalizado)
def lin():
    print('-'*30)


#Programa Principal:
lin()
print('  Curso em Vídeo  ')
lin()
print('  Aprenda Python  ')
lin()
print('  Paloma Gonçalves  ')
lin()

'''


'''
#Criação de um comando novo (personalizado)
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


#Programa Principal:
mensagem('  Curso em Vídeo  ')
mensagem('  Aprenda Python  ')
mensagem('  Paloma Gonçalves  ')
'''

'''
#Criação de um comando novo (personalizado)
def soma(a,b):
    print('-'*30)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma e {a} e {b} é igual a {s}')
    print('-'*30)


#Programa Principal:
soma(4,5)
soma(8,9)
soma(2,1)

'''

'''
#Criação de um comando novo (personalizado)
def contador(* núm): #pega todos os parâmetros e joga dentro de núm
    print('-'*30) #desempacotamento
    tam = len(núm) #o núm é uma tupla
    print(f'Os números são {núm} e apresentam o tamanho de {tam}')
    print('-'*30)


#Programa Principal:
contador(4,5,6,3)
contador(8,9,2,5,8)
contador(2,1)

'''

'''
#Criação de um comando novo (personalizado)
def dobra(lst):
    print('-'*30)
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+= 1




#Programa Principal:
valores = [6,3,2,5,9,8,7]
print(valores)
dobra(valores)
print(f'Valores dobrados {valores}')

'''
