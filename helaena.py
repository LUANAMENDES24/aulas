#FUNCAO RECURSIVA FIBONACCI
#SEQUENCIA FIBONACCI: 0 1 1 2 3 5 8 13 21 34 55 89 ...
#    posicoes:  1ª  2ª  3ª  4ª  5ª  6ª  7ª  8ª  9ª  10ª  11ª ...
def fibonacci(posicao):
    if posicao <= 1:
        return posicao
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)
a = int(input('DIGITE A POSICAO PARA O VALOR FIBONACCI:'))
res = fibonacci(a)
print('NA POSICAO %dª O VALOR E \033[1;033m%d' % (a, res))
#('NA %dª' POSICAO O VALOR FIBONACCI E:\033[1;33m %d' % (a, res))