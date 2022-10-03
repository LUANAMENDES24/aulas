

def impar(numero):
    resposta = ""
    condicao= numero % 2 ==0
    if condicao:
        resposta = "par"
    
    else:
        resposta = "impar"

    return resposta, numero


r,n = impar(3)

print(r, n)