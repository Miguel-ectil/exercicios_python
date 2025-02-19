# Anotando a formula pois não a sei de cabeça

# -- Converte para Celsius usando a fórmula (C = (F - 32) * 5 / 9) -->
# -- Subtraímos 32 de Fahrenheit, multiplicamos por 5 e dividimos por 9 --!

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"A temperatura em Celsius é: {celsius:.2f}°C")
