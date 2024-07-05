import random

vitorias_usuario = 0
vitorias_computador = 0

opcoes = ["pedra", "papel", "tesoura"]

while True:
  input_usuario = input("Digite Pedra/Papel/Tesoura ou Q para sair: ").lower()
  if input_usuario == "q":
    break

  if input_usuario not in opcoes:
    continue

  numero_aleatorio = random.randint(0, 2)

  escolha_computador = opcoes[numero_aleatorio]
  print("O computador escolheu", escolha_computador + ".")

  if escolha_computador == "pedra" and input_usuario == "tesoura":
    print("Vitória da máquina")
    vitorias_computador += 1

  if escolha_computador == "pedra" and input_usuario == "papel":
    print("Você ganhou!")
    vitorias_usuario += 1

  if escolha_computador == "pedra" and input_usuario == "pedra":
    print("Empate")

  if escolha_computador == "papel" and input_usuario == "tesoura":
    print("Você ganhou!")
    vitorias_usuario += 1

  if escolha_computador == "papel" and input_usuario == "pedra":
    print("Vitória da máquina")
    vitorias_computador += 1

  if escolha_computador == "papel" and input_usuario == "papel":
    print("Empate")

  if escolha_computador == "tesoura" and input_usuario == "tesoura":
    print("Empate")

  if escolha_computador == "tesoura" and input_usuario == "pedra":
    print("Você ganhou!")
    vitorias_usuario += 1

  if escolha_computador == "tesoura" and input_usuario == "papel":
    print("Vitória da máquina")
    vitorias_computador += 1
  else:
    None


print(f'A máquina venceu {vitorias_computador} vezes.')
print(f'Você veucenu {vitorias_usuario} vezes.')
print("Adeus!")