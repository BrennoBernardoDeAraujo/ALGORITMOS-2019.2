"""
A04.Q001 -  Implemente um programa que exiba a tabuada do 2 ao 9 """


for tabuada in range(1, 10):
    print('-----------------------')
    print()
    print(f'Tabuada de {tabuada}')
    print()

    for numero in range(1, 11):
        print(f'{tabuada} X {numero} = {tabuada * numero}')
    print()
