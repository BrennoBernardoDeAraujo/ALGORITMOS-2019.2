"""
A04.Q008 -  Crie um algoritmo que simule o funcionamento de
um caixa de supermercado. O caixa fica aberto até o fim do 
expediente e pode processar a compra de vários clientes.

- Cada cliente pode comprar vários itens. Ao ler cada item deve ser
    exibida uma mensagem para o operador do caixa perguntando se há mais 
    itens a serem processados. Ao final, exiba quanto a compra custou ao cliente.
    E então solicite do operador do caixa a informação se deseja fechar o caixa.
- Quando o caixa for fechado, exiba quanto de dinheiro aquele caixa apurou no dia. """

sair = input('Deseja fechar o caixa? [sim] ou [nao]: ')

apurado = 0

while sair == 'nao':
    preco_total = 0

    cliente = input('deseja processar mais itens? [sim] ou [nao]: ')
    
    while cliente == 'sim':
        item = input('Adicione um Item: ')
        preco = float(input('Qual o valor do item: '))
        preco_total = preco_total + preco

        cliente = input('deseja processar mais itens? [sim] ou [nao]: ')
        print(f'Compra do cliente é: {preco_total:.2f}')        

        
    apurado = apurado + preco_total
    sair = input('Deseja fechar o caixa? [sim] ou [nao]')

print(f'O apurado do dia foi: {apurado:.2f}')


    
