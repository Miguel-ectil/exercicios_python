# Série de Fibonacci é 

# Forma mais simples
n = int(input("Quantos termos da série de Fibonacci você deseja? "))

a, b = 1, 1
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b

# -- Forma detalhada --

# n = int(input("Quantos termos da série de Fibonacci você deseja? "))

# if n <= 0:
#     print("Por favor, insira um número inteiro positivo.")
# else:
#     # Definindo os dois primeiros termos da série
#     primeiro_termo = 1
#     segundo_termo = 1

#     # Exibe os termos iniciais se o usuário solicitar 1 ou 2 termos
#     if n == 1:
#         print(primeiro_termo)
#     elif n == 2:
#         print(primeiro_termo, segundo_termo)
#     else:
#         print(primeiro_termo, segundo_termo, end=" ")

#         # Calcula os próximos termos da série
#         for i in range(3, n + 1):  # Começa do terceiro termo até o n-ésimo termo
#             proximo_termo = primeiro_termo + segundo_termo  # Soma dos dois anteriores
#             print(proximo_termo, end=" ")

#             # Atualiza os valores para o próximo ciclo
#             primeiro_termo = segundo_termo
#             segundo_termo = proximo_termo

#         print()  # Apenas para pular a linha após exibir a sequência
