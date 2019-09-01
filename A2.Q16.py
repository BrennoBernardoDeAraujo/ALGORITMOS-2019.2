# 16.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.


kgmaca = float(input("Digite a quantidade (KG) de maçãs: "))
kgmorango = float(input("Digite a quantidade (KG) de morangos: "))
Vmaca = float(kgmaca * 1.8)
Vmorango = float(kgmorango * 2.5)
TOTAL = float(Vmaca + Vmorango)

if kgmaca > 5:
        Vmaca = float(kgmaca * 1.5)
if kgmorango > 5:
        Vmorango = float(kgmorango * 2.2)
if (kgmaca + kgmorango) > 8 or (Vmaca + Vmorango) > 25:
        TOTAL = float((Vmaca + Vmorango) * 0.9)
print("O total a ser pago é: ",TOTAL)