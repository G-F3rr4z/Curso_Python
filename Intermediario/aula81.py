# Crie um sistema de perguntas e respostas


perguntas = [{
        'Pergunta': 'Qual o nome do seu persoangem favorito ?',
        'Opcoes' : ['Homen de Ferro', 'Homen aranha', 'Batmna', 'Super Homem'],
        'Resposta': 'Homen de Ferro',
    },

    {
        'Pergunta': 'Qual o seu carro favorito ?',
        'Opcoes' : ['Porshe', 'Gol Bola', 'Nissan GTR', 'Golk MK7'],
        'Resposta': 'Nissan GTR',
    },

    {
        'Pergunta': 'Qual o seu jogo favorito ?',
        'Opcoes' : ['CSGO', 'PUBG', 'GTA V', 'Asseto Corsa'],
        'Resposta': 'PUBG',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(pergunta['Opcoes']):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma Opcao: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')
    print()

print('Voce acertou', qtd_acertos, 'de', len(perguntas), 'perguntas!')



