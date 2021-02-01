from random import randint

print('Vamos Jogar Jokenpo\n 0 = Sim\n 1 = Nao')
print(' ')

jokenpo = ['Papel', 'Pedra', 'Tesoura']
jogar = int(input('Digite sua Opçao: '))
print('')

if jogar >= 2:
    print('Opcao Invalida')

while jogar < 1:
    print('Faça Sua Escolha\n 0 = Papel\n 1 = Pedra\n 2 = Tesoura\n')
    escolha = int(input('Digite sua Escolha: '))

    if escolha not in jokenpo:
        print('Opcao Invalida')

    computador = randint(0, 2)
    jogo1 = jokenpo[escolha]
    jogo2 = jokenpo[computador]


    print(f'Sua Escolha Foi: {jogo1}\nO Computador Escolheu: {jogo2}')

    if jogo1 == jogo2:
        print('*' * 7)
        print('Empatou')
        print('*' * 7)
        print('')

    elif escolha == 0 and computador == 1 or escolha == 1 and computador == 2 or escolha == 2 and computador == 0:
        print('*' * 11)
        print('Voce Ganhou')
        print('*' * 11)
        print('')

    elif computador == 0 and escolha == 1 or computador == 1 and escolha == 2 or computador == 2 and escolha == 0:
        print('*' * 11)
        print('Voce Perdeu')
        print('*' * 11)
        print('')

    print('Que Jogar mais\n 0 = Sim\n 1 = Nao')
    print(' ')
    jogar = int(input('Digite sua Opçao: '))
    print('')

    if jogar >= 2:
        print('Opcao Invalida')

else:
    print('Fim De Jogo')
