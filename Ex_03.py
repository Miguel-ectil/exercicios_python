ganhoHora = float(input("Quanto você ganha por hora trabalhadas: "))
horaTrabalha = int(input("Quantas horas você trabalhou no mês: "))

salarioBruto = ganhoHora * horaTrabalha

descontoIR = salarioBruto * 0.11  
descontoINSS = salarioBruto * 0.08  
descontoSindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (descontoIR + descontoINSS + descontoSindicato)

print("\n===== Detalhamento do Salário =====")
print(f"+ Salário Bruto: R$ {salarioBruto:.2f}")
print(f"- IR (11%): R$ {descontoIR:.2f}")
print(f"- INSS (8%): R$ {descontoINSS:.2f}")
print(f"- Sindicato (5%): R$ {descontoSindicato:.2f}")
print(f"= Salário Líquido: R$ {salarioLiquido:.2f}")