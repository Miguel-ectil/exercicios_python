
cont = 1
quantPares = 0
quantImpares = 0
while cont < 4:
  num = int(input(f"Digite o {cont} número: "))
  cont += 1
  if num % 2 == 0:
    quantPares += 1 
    
    if num % 2 != 0:
      quantImpares += 1
print(f"A quantidade de números pares é: {quantImpares}, e a de números impares é {quantImpares}")
