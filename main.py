from random import randint

print('Vamos Jogar Jokenpo')
print(' ')
print('Faça Sua Escolha\n 0 Papel\n 1 Pedra\n 2 Tesoura\n')


jokenpo = ['Papel', 'Pedra', 'Tesoura']
escolha = int(input('Digite sua Escolha: '))
computador = randint(0, 2)

jogo1 = jokenpo[escolha]
jogo2 = jokenpo[computador]

if escolha < 3:
    print(f'Sua Escolha Foi: {jogo1}\nO Computador Escolheu: {jogo2}')
    if jogo1 == jogo2:
        print('Empatou')

    # preciso saber como fazer a parte de perder e ganhar
    elif jogo1[0] <= jogo2[1] or jogo1[1] <= jogo2[2] or jogo1[2] >= jogo2[0]:
        print('voce Ganhou')
    elif jogo1[1] >= jogo2[0] or jogo1[2] >= jogo2[1] or jogo1[0] == jogo2[2]:
        print('voce Perdeu')

else:
    print('Opçao Errada')
