cont = 1
quantPares = 0
quantimpares = 0

while cont <= 10:
  num = int(input(f"Digite o {cont}º: "))
  cont += 1

  if num % 2 == 0:
    quantPares += 1
  elif num % 2 == 1:
    quantimpares += 1 
print(f"você digitou {quantPares} números pares e {quantimpares} números impares")