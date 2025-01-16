'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
guarde esses resultados em um dicionario. No final
coloque em ordem, sabendo que o vencedor tirou o maior numero no dado.'''
from random import randint # biblioteca para sorteio
from time import sleep # biblioteca para tempo
from operator import itemgetter #biblioteca para selecionar itens no dcionario
jogadores = dict()
for c in range(1,5):
    jogadores[f'jogador {c}'] = randint(1,6)
print('     Valores sorteados:')
sleep(1)
for v, k in jogadores.items():
    print(f' O {v} Jogou o número {k} no dado.')
    sleep(1)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('   ==RANKING DO JOGADORES==')
sleep(1.5)
for i, v in enumerate(ranking):
    print(f'  {i+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(1)
print('-=' * 20)