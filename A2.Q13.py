numero = int(input(": "))
centena = int(numero/100)
dezena = int((numero-(centena*100))/10)
unidade = int(numero - (centena*100 + dezena*10))
notas100 = centena
notas50 = 0
notas10 = dezena
notas5 = 0
notas1 = unidade

if dezena > 5:
    notas50 =  1  
    notas10 = dezena - 5
    if unidade > 5:
        notas5 =  1 
        notas1 = unidade - 5
    if notas100 > 1:
        print(notas100,"notas de 100 ,",end="")
    if notas100 == 1:
        print(notas100,"nota de 100 ,",end="")
    if notas50 > 1:
        print(notas50,"notas de 50 ,",end="")
    if notas50 == 1:
        print(notas50,"nota de 50 ,",end="")
    if notas10 > 1:
        print(notas10,"notas de 10 ,",end="")
    if notas10 == 1:
        print(notas10,"nota de 10 ",end="")
    if notas5 > 1:
        print(notas5,"notas de 5 ,",end="")
    if notas5 == 1:
        print(notas5,"nota de 10 ,",end="")
    if notas1 >= 1:
        print(notas1,"notas de 1 .",end="")
    if notas10 == 1:
        print(notas1,"nota de 10 .",end="")