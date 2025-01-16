'''Faça um programa que leia nome e media de um aluno, guardando em um dicionário.
No final mostre o conteudo da estrutua na tela.'''
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] > 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Média'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')