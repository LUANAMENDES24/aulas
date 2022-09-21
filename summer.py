def soma(n1, n2):
    s = n1 + n2
    return s

def sub(n1, n2):
    s = n1 - n2
    return s

def mult(n1, n2):
    s = n1 * n2
    return s
    
def div(n1, n2):
    s = n1 / n2
    return s

def resto(n1,n2):
    s =  n1 // n2
    d = n1 % n2      
    return  s , d 

print("emily, por favor, escolha um operação matemágica")

print("1- soma")
print("2- subtração")
print("3- divisão")
print("3- multiplicação")
print("5- resto")

opcao = input("opção escolhida: ")

n1 = input("digite o primeiro numero: ")
n2 = input("digite o segundo numero: ")

n1 = int(n1)
n2 = int(n2)

if opcao == "1":
    print(soma(n1, n2))
elif opcao == "2":
    print(sub(n1, n2))
elif opcao == "3":
    if (n2 == 0):
        print("inexistente")
    else:
        print(div(n1, n2))  
elif opcao == "4":
    print(mult(n1, n2))
elif opcao == "5":
        print(resto(n1, n2))        