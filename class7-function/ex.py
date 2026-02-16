# Escreva uma function que recebe um objeto de coleção (lista, tupla etc...) e vai retornar o valor do maior numero dentro dessa colecao

# FORMA MAIS LOGICA, PERCORRENDO A LISTA TODA
def maiorNumero(colecao):
    # Comecamos assumindo que o primeiro numero é o maior
    maior = colecao[0]

    # Percorremos cada item da colecao
    for i in colecao:
        # se o item atual for maior que o nosso 'maior' salvo, vamos atualizar quem sera o maior
        if i > maior:
            maior = i
    return maior
# fim da function

#testando
numeros = [10, 20, 321, 54, 3, 432, 55, 65, 1, 2]
print(maiorNumero(numeros))

#-------------------------------------------------------------------------

# Forma Nutella
def maiorNumeroNutella(lista):
    return max(lista)
#testando
numeros = [10, 20, 321, 54, 3, 432, 525, 65, 1, 2]
print(maiorNumeroNutella(numeros))
