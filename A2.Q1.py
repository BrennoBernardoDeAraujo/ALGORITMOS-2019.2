# 1. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite "F" para Feminino, "M" para Masculino: ').upper())
if sexo == 'M':
    print('Masculino.')
elif sexo == 'F':
    print('Feminino.')
else:
    print('Sexo Inválido.')

# A funçao ".upper()" converte caixa baixa em alta(ou minúscula em maiúscula) nao era necessário 
# seu uso pois é informado ao o usuário para digitar em maiúsculo mas aumenta a eficiencia do programa.