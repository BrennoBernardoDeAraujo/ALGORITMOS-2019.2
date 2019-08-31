# 8.Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que 
# o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#  O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) Sindicato ( 3%)             : R$   33,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$   88,00
#        Salário Líquido                : R$  1012,00

VH = float(input('Valor da hora de trabalho: '))
HT = float(input('Quantidade de hora trabalhada no mês: '))
SB = (VH*HT)
DS = (SB/100)*3
fgts = (SB/100)*11
ir = 0
if SB <= 900:
    SL = (SB - DS)
    print(
    "Salário Bruto:",SB,
    "\n(-) IR :",ir,
    "\n(-) Sindicato :",DS,
    "\nFGTS (11%):",fgts,
    "\nTotal de descontos:",ir + DS,
    "\nSalário Líquido:",SL)
elif SB <= 1500:
    ir = (SB/100)*5
    sl = SB - DS - ir
    print(
    "Salário Bruto:",SB,
    "\n(-) IR :",ir,
    "\n(-) Sindicato :",DS,
    "\nFGTS :",fgts,
    "\nTotal de descontos:",ir + DS,
    "\nSalário Líquido:",sl)
elif SB <= 2500:
    ir = (SB/100)*10
    Sliq = SB - DS - ir
    print(
    "Salário Bruto:",SB,
    "\n(-) IR :",ir,
    "\n(-) Sindicato :",DS,
    "\nFGTS (11%):",fgts,
    "\nTotal de descontos:",ir + DS,
    "\nSalário Líquido:",Sliq)   
else:
        ir = (SB/100)*20
        SalarioLiquido = SB - DS - ir
        print(
    "Salário Bruto:",SB,
    "\n(-) IR :",ir,
    "\n(-) Sindicato :",DS,
    "\nFGTS :",fgts,
    "\nTotal de descontos:",ir + DS,
    "\nSalário Líquido:",SalarioLiquido)
