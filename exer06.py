idade = []
altura = []

for valor in range(0, 5):
    idade.append(int(input("Idade: ")))
    altura.append(float(input("Altura: ")))

print("ORDEM INVERSA: ")
for valor in range(0, 5):
    print(idade[len(idade)-1-valor])
    print(altura[len(altura)-1-valor])