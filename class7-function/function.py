def soma(numero1, numero2):
    resposta = numero1 + numero2
    return resposta

retorno = soma(43, 65)

print(retorno)

# -------------------------------------------------

def dizOi () :
    print("Oi")

dizOi()
# Posso colocar ela em loop assim
#       while True:
#           dizOi()

# -------------------------------------------------

def temSeteItens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
    

if temSeteItens("casaraoo"):
    print("Realmente tem sete letras")
else:
    print("Nao tem sete letras")