# 15.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:até 20 litros, desconto de 3% por litroacima de 20 litros, desconto de 5% por litroGasolina:
# até 20 litros, desconto de 4% por litroacima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

l = float(input("Digite a quantidade de litros comprados: "))
tipo = input("A-alcool, G-gasolina: ")

if tipo == "A":
	preco = 1.9
	if l <= 20:
		desc = 3
	elif l > 20:
		desc = 5
elif tipo == "G":
	preco = 2.5
	if l <= 20:
		desc = 4
	elif l > 20:
		desc = 6

total = l * preco - (l * preco * desc / 100)

print("O valor a ser pago para" ,l ,"litros de",tipo,"é: R$",total)