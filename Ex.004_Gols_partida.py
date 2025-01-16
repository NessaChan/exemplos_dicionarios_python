'''Crie um prgrama que gerencia o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e qantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario.
Incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partida = list()
jogador.clear()
jogador['Jogador'] = str(input('Nome do Jogador: '))
totgol = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
for p in range(0,totgol):
    partida.append(int(input(f'   Quantos gols na partida {p + 1}: ')))
jogador['Gols'] = partida[:]
jogador['Total'] = sum(partida)
print('-=' * 30)
print('   = Dados do Jogador =')
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k}:  {v}')
print('-=' * 20)

    
