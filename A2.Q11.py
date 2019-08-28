# Faça um Programa que peça um número correspondente a um determinado ano
#  e em seguida informe se este ano é ou não bissexto 

ano = input("digite um ano (XXXX): ")
if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
    print (ano, " O ano informado é Bissexto")
else:
    print (ano, " O ano informado não é bissexto")