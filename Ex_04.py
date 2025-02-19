n1 = float(input("Digite a sua 1º nota: "))
n2 =  float(input("Digite a sua 2º nota: "))

media = ( n1 + n2 ) / 2

if media >= 7 and media < 10:
  print(f"Nota: {media}, Aprovado")
elif media <= 7:
  print(f"Nota: {media}, Reprovado")
else:
  if media == 10:
    print("Aprovado com Distinção")
    