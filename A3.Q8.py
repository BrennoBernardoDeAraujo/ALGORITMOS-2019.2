# 8.Faça um programa que receba dois números inteiros e gere 
# os números inteiros que estão no intervalo compreendido por eles.

num1=int(input("digite um numero: "))
num2=int(input("digite outro numero: "))
while num2<num1:
	num1=int(input("digite um numero: "))
	num2=int(input("digite outro numero: "))
else:
	for i in range(num1+1,num2,1):
		print(i)