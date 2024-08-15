import random, sys

print('-'*40)
print('PEDRA, PAPEL, TESOURA\n')
print('-'*40)

# números de vitórias, derrotas e empates.
vitorias = 0
derrotas = 0
empates = 0

while True:  # O loop do jogo principal.
    print('_'*40)
    print(f'\n{vitorias} Vitórias | {derrotas} Derrotas | {empates} Empates\n')
    print('-'*40)
    
    while True:  # O loop de entrada do jogador.
        print('Digite seu movimento: (p)edra (a)papel (t)esoura ou (s)air')
        movimento_jogador = input()
        
        if movimento_jogador == 's':
            sys.exit()  # Saia do programa.
        
        if movimento_jogador in ('p', 'a', 't'):
            break  # Sai do loop de entrada do jogador.
        print('Digite um de p, a, t, ou s.')

    # Exibe o que o jogador escolheu:
    if movimento_jogador == 'p':
        print('PEDRA versus...')
    elif movimento_jogador == 'a':
        print('PAPEL versus...')
    elif movimento_jogador == 't':
        print('TESOURA versus...')

    # Exibe o que o computador escolheu:
    numero_aleatorio = random.randint(1, 3)
    
    if numero_aleatorio == 1:
        movimento_computador = 'p'
        print('PEDRA')
    elif numero_aleatorio == 2:
        movimento_computador = 'a'
        print('PAPEL')
    elif numero_aleatorio == 3:
        movimento_computador = 't'
        print('TESOURA')

    # Exibe e registra a vitória/derrota/empate:
    if movimento_jogador == movimento_computador:
        print('É um empate!')
        empates += 1
    elif movimento_jogador == 'p' and movimento_computador == 't':
        print('Você venceu!')
        vitorias += 1
    elif movimento_jogador == 'a' and movimento_computador == 'p':
        print('Você venceu!')
        vitorias += 1
    elif movimento_jogador == 't' and movimento_computador == 'a':
        print('Você venceu!')
        vitorias += 1
    elif movimento_jogador == 'p' and movimento_computador == 'a':
        print('Você perdeu!')
        derrotas += 1
    elif movimento_jogador == 'a' and movimento_computador == 't':
        print('Você perdeu!')
        derrotas += 1
    elif movimento_jogador == 't' and movimento_computador == 'p':
        print('Você perdeu!')
        derrotas += 1
