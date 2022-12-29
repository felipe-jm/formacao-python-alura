import random

def jogar_adivinhacao():
  print("Bem-vindo ao jogo da adivinhação")

  numero_secreto = random.randrange(1, 101)
  total_tentativas = 0
  pontos = 1000

  print("Qual o nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível: "))

  if nivel == 1:
    total_tentativas = 20
  elif nivel == 2:
    total_tentativas = 10
  else:
    total_tentativas = 5

  for rodada in range(1, total_tentativas):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute_str = input("Digite o seu número: ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    if chute < 1 or chute > 100:
      print("Você deve digitar um número entre 1 e 100!")
      continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
      print(f"Você acertou e fez {pontos} pontos!")
      break
    else:
      pontos_perdidos = abs(numero_secreto - chute)
      pontos -= pontos_perdidos
      if maior:
          print("O seu chute foi maior que o número secreto")
          if rodada == total_tentativas:
              print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
          elif menor:
              print("Você errou! O seu chute foi menor do que o número secreto.")
              if rodada == total_tentativas:
                  print(f"O número secreto era {numero_secreto}. Você fez {pontos}")


  print(f"Fim do jogo! O número era: {numero_secreto}")

if __name__ == "__main__":
  jogar_adivinhacao()