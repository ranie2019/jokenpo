from random import randint

print('Vamos Jogar Jokenpo')
print(' ')
print('Faça Sua Escolha\n 0 = Papel\n 1 = Pedra\n 2 = Tesoura\n')


jokenpo = ('Papel', 'Pedra', 'Tesoura')
escolha = int(input('Digite sua Escolha: '))
computador = randint(0, 2)

jogo1 = jokenpo[escolha]
jogo2 = jokenpo[computador]

print(f'Sua Escolha Foi: {jogo1}\nO Computador Escolheu: {jogo2}')

if jogo1 == jogo2:
    print('Empatou')

elif escolha == 0 and computador == 1 or escolha == 1 and computador == 2 or escolha == 2 and computador == 0:
    print('voce Ganhou')

elif computador == 0 and escolha == 1 or computador == 1 and escolha == 2 or computador == 2 and escolha == 0:
    print('voce Perdeu')
