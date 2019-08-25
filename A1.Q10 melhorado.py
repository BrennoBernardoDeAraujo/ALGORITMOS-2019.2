# 10. Faça um programa que receba as dimensões de uma sala de aula (comprimento e
# largura) e as dimensões de uma carteira. Considerando que:
# - Entre duas fileiras deve haver 0,5 m de espaço;
# - Entre duas cadeiras na mesma fileira deve haver 0,2 m de espaço;
# - Deve ser reservada ao professor um espaço de 1,5 m de comprimento;
# Calcule quantas carteiras cabem na sala de aula.

CS =  float (input("Comprimento da sala: "))
LS =  float (input("Largura da sala: "))
CC =  float (input("Comprimento da carteira: "))
LC =  float (input("Largura da carteira: "))
qcc = int (CS - 1.3)//(CC + 0.2)
QCL = int (LS - 0.5)//(LC + 0.5)
QCT = int (qcc * QCL)
print ("Cabem na sala de aula",QCT,"Carteiras" )

# Siginificado das siglas:

# CS = Comprimento da sala
# LS = Largura da sala
# CC = Comprimento da carteira
# LC = Largura da carteira
# qcc = Quantidade de carteiras numa fila
# QCL = Quantida de carteiras paralelas na horizontal
# QCT = Quantidade total de carteiras que cabem na sala