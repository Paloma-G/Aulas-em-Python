'''
#Fatiamento de string
num = 12345678
num = str(num)
for i in num:
    print(i)
'''


'''
#Comado While
num = 12345678
while(num > 0):
    resto = (num % 10)
    num = (num //10) #divisão inteira....some o ultimo
    print(resto) #fatia os numeos

'''

'''
#Comandos ifs para variáveis booleanas
a == b: se a é igual b
a != b: se a é diferente de b
a >= b: se a é maior do que b
a <= b: se a é menor do que b
and
or
a = 5 > 4  -> True
a = not 5 > 4 -> False0

'''

'''
num = int(input('digite um número: '))
primo = 1
for i in range(2, num):
    if(num % i == 0):
        primo = 0
if (primo == 1):
    print(f'O úmero {num} é primo')
else:
    print(f'{num} Não é primo')

'''

'''
num = int(input('digite um número: '))
primo = True
for i in range(2, num):
    if(num % i == 0):
        primo = False
if (primo):
    print(f'O úmero {num} é primo')
else:
    print(f'{num} Não é primo')

'''

