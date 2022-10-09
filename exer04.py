num = int(input("Digite um número inteiro: "))
resto = num%2
if resto == 0:
    print("{} é PAR!".format(num))
else:
    print("{} é IMPAR!".format(num))