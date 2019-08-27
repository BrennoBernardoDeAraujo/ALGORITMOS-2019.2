# 2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

LETRA = str(input('Digite uma letra: ').lower())
if LETRA == 'a' or LETRA == 'e' or LETRA == 'i' or LETRA == 'o' or LETRA == 'u':
    print('A letra',LETRA,'é vogal')
else:
    print('A letra',LETRA,'é consoante')

# A funçao ".lower" é o oposto da funçao ".upper" 