"""
8. Dadas duas listas de tamanho N, faça uma função que diga se as mesmas possuem
conteúdo igual. """
tamanho_lista = int(input('Digite o tamanho das lista: '))
lista = [0] * tamanho_lista
lista2 = [0] * tamanho_lista


print('Lista 01')
for i in range(tamanho_lista):
    lista[i] = int(input('Adicione os numeros da primeira lista: '))

print('Lista 02')
for i in range(tamanho_lista):
    lista2[i] = int(input('Adicione os numeros da segunda lista: '))


def ver(tam):
    for i in range(tam):
        if lista[i] == lista2[i]:
            return True


verdadeira = ver(tamanho_lista)

print(f'Números digitados da 1ª Lista:{lista}')
print(f'Números digitados da 2ª Lista:{lista2}')

if verdadeira:
    print('Possui elementos iguais.')
else:
    print('Não possui elementos iguais.')
