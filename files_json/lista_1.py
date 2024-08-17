frutas = ['banana', 'maça', 'tomate', 'abacaxi']
print(frutas, 'LISTA COMPLETA')
print()
print(frutas[0], 'Pegando apenas um item da lista com [0]')
print()
print(frutas[3], 'PEPGANDO O ULTIMO INDEX DA LISTA QUE É [3]')
print()
print('Tamanho da lista')
print(len(frutas))
print()
print('Adicionado um novo valor a lista')
frutas.append('manga')

print(frutas)
frutas.sort()  # ordenado uma lista por alfabeto
print(frutas)