# 9. Crie um programa que pergunta o nome do usuário e o ano de nascimento do usuário e calcula 
# qual idade ele tem (ou terá, se ainda não fez aniversário neste ano). Ex.: Nome = Carlos, Ano = 1999.
# O programa mostra a mensagem: “Carlos tem 20 anos”.

NOME = str(input("Qual o seu nome: "))
ANOdeNASC = int (input("Em que ano voce nasceu: "))
IDADE = int (2018 - ANOdeNASC)
print (NOME," tem ",IDADE,"anos")

# Siginificado das siglas:

# NOME = Nome do usuário
# ANOdeNASC = Ano que nasceu
# IDADE = idade que ele tem (ou terá, se ainda não fez aniversário neste ano)