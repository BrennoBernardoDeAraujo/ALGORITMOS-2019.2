# 9.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada. 
# A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

while 1==1:
    tabuada=int(input("De qual número de 1 a 10 voce deseja ver a tabuada?: "))
    numero = tabuada
    cont=0
    while cont <= 9:
        cont = cont+1
        print(numero,"*",cont,"=",tabuada)
        tabuada = tabuada + numero
