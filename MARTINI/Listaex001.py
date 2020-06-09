'''
#Lista 1
1)
nome = input('Qual o seu nome?')
altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso?'))
IMC = (peso / (altura * altura)) ;
print("{0} tem {1} kilos e altura de {2} e portanto o IMC é de {3:4.2f}".format(nome,peso,altura,IMC))'''


'''
#2)
metros = float(input("Qual é o valor em metros?"))
mm = float(metros)*1000;
print("A conversão do valor {0} metros em mm é {1:2.2f}".format(metros,mm))

# para int %d, para str %c, para float %f

# colocar 3 aspas simples antes e depois do comentario, para texto grande '''

'''
#3)
dia = int(input("Digite o dia "))
hora = float(input("Digite às horas "))
min =  float(input("Digite os minutos "))
seg =  int(input("Digite os segundos "))

res = (int(dia)*86400)+(float(hora)*3600)+(float(min)*60)+ (int(seg));

print("Total de segundos {}".format(res))
'''

'''
#4)
sal = float(input("Qual é o seu salário? "))
p = float(input("Qual é a porcentagem de aumento? "))
a = float(sal)*(float(p));
res = float(sal)*(1+float(p));
print('O valor do aumento é de {} e o novo salário é de {}'.format(a,res))
'''

'''
#5)
km = float(input("Qual a quantidade em KM percorrida? "))
dia = int(input("Qual a quantidade de dias que o carro foi alugado? "))

km = float(km)* 0.15;
dia = int(dia)* 60;

res = km + dia;

print('O preço a pagar é de {}'.format(res))
'''