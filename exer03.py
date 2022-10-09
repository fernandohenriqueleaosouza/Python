nome = str(input("Digite o seu nome: "))
salhora = float(input("Valor que ganha por hora: "))
htrabalhada = float(input("Digite o valor de horas trabalhadas: "))

salbruto = salhora * htrabalhada
pgir = (salbruto*11)/100
pginss = (salbruto*8)/100
pgsindicato = (salbruto*5)/100
desconto_total = pgir + pginss + pgsindicato
saliquido = salbruto - desconto_total

print("{}, Segue abaixo o calculo do salário líquido do mês:".format(nome))
print("Salário Bruto: {:.2f};\nIR: {:.2f};\nINSS: {:.2f};\nSindicato: {:.2f};\nTotal de desconto: {:.2f}; e,\nSalário líquido: {:.2f}".format(salbruto, pgir, pginss, pgsindicato, desconto_total, saliquido))