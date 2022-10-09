peso, excesso, multa = 0, 0, 0

peso = float(input("Digite o peso total da pesca: "))
if peso <= 50:
    print("Peso total da pesca foi de {}, não excedeu o peso estipulado por lei.".format(peso))
else:
    excesso = float(peso - 50)
    multa = float(excesso * 4)
    print("Peso total: {:.2f};\nPeso excedido: {:.2f}; e,\nValor total da multa: R${:.2f}".format(peso, excesso, multa))