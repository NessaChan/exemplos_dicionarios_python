'''Aprimore o DESAFIO 004 para que ele funcione com varios jogadores, 
inclundo o sistema de visualização de detalhes do aproveitamento de cada jogador.'''
turma = list()
jogador = dict()
partida = list()
while True:
    jogador.clear()
    jogador['Jogador'] = str(input('Nome do Jogador: '))
    totgol = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
    partida.clear()
    for p in range(0,totgol):
        partida.append(int(input(f'   Quantos gols na partida {p + 1}: ')))
    jogador['Gols'] = partida[:]
    jogador['Total'] = sum(partida)
    turma.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S[Para Sim] ou N[Para Não].')
    if resp == 'N':
        break
print('-=' * 30)
print('         = Dados do Jogador =')
print('-=' * 20)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(turma):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-=' * 30)
while True: 
    busca = int(input('Mostrar dados de qual jogador?[999 para parar!] '))
    if busca == 999:
        break
    if busca >= len(turma):
        print(f'ERRO!Não existe jogador com código {busca}')
    else:
        print(f'    LEVANTAMENTO DO JOGADOR {turma[busca]["Jogador"]}:')
        for i, g in enumerate(turma[busca]['Gols']):
            print(f'    No Jogo {i+1} fez {g} gols.')
print('Fim do Programa!')
