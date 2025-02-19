import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def jogar(self):
        print(f"Bem-vindo ao jogo, {self.nome}!")
        ponto = self.jogarDados()
        print(f"Sua primeira jogada foi {ponto}")

        if ponto == 7 or ponto == 11:
            print("Você venceu!!! NATURAL 🎉")
        elif ponto in [2, 3, 12]:
            print("Perdeu!!! CRAPS 💀")
        else:
            print(f"Fase de PONTO! Seu ponto é {ponto} 🎯")
           
            while True:
                novoPonto = self.jogarDados()
                print(f"Você tirou {novoPonto}")

                if novoPonto == ponto:
                    print("Você Venceu! 🎉")
                    break
                elif novoPonto == 7:
                    print("Você Perdeu! 💀")
                    break

    def jogarDados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        soma = dado1 + dado2
        return soma

jogador1 = Jogador("Caio")
jogador1.jogar()
