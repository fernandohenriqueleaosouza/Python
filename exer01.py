nome = str(input("Digite o seu nome: "))
sexo = int(input("{}, Digite número 1 para Masculino ou 2 para Feminino: ".format(nome)))
h = float(input("{}, Digite a sua altura: ".format(nome)))
ideal = float(0)

if sexo == 1:
    ideal = (72.7*h) - 58
elif sexo == 2:
    ideal = (62.1*h) - 44.7
else:
    print("Erro, seu sexo não foi identificado!")

print("{}, o seu peso ideal é de {:.2f}".format(nome, ideal))