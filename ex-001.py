import random

numero = random.randint(1, 100)
tentativas = 0

print("Bem-vindo ao jogo da adivinhação!")
print("Eu escolhi um número entre 1 e 100. Você tem 10 tentativas para adivinhar.")

while tentativas < 10:
   palpite = int(input("Digite o seu palpite: "))
   tentativas += 1

   if palpite == numero:
       print(f"Parabéns! Você acertou o numero em {tentativas} tentativas.")
       break
   elif palpite < numero:
        print("O número é maior. Tente novamente.")
   else:
        print("O número é menor. Tente novamente.")
else:
    print(f"Você perdeu! O número era {numero}.")