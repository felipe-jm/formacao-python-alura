import forca
import adivinhacao

def escolher_jogo():
  print("Escolha o seu jogo!")

  print("(1) Forca (2) Adivinhação")

  jogo = int(input("Qual jogo?"))

  if jogo == 1:
    print("Jogando Forca")
    forca.jogar_forca()
  elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao.jogar_adivinhacao()

if __name__ == "__main__":
  escolher_jogo()