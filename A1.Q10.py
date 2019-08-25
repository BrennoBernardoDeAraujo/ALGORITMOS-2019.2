CS =  float (input)("Comprimento da sala: ")
LS =  float (input("Largura da sala: "))
CC =  float (input("Comprimento da carteira: "))
LC =  float (input("Largura da carteira: "))
QCC = float (CS - 1.3)//(CC + 0.2)
QCL = float (LS - 0.5)//(LC + 0.5)
totalC = float QCC * QCL
print ("Cabem na sala de aula ",totalC," Carteiras" )