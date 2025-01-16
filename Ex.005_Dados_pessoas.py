'''Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um diconario.
 e todos os diconarios em uma lista. No final, mostre:
 a) Quants pessas fpram cadastradas.
 B) A media de idade do grupo.
 C) Uma lista com as mulhres.
 D) Uma lista com todos as pessoas com idade acima da media.'''
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['Sexo'] = str(input('Digite o sexo:[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in  'MF':
            break
        print('ERRO! Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
for k, v in enumerate(galera):
    print(f'pessoa {k+1} = {v}')
print('-=' * 30)
print('ANÁLISE DOS DADOS CADASTRADOS:')
print(f'Foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média de idade do  grupo é {media:5.2f} anos')
print(f'As mulheres do grupo foram: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('As pessoas acima da média foram: ', end='')

for c in galera:
    if c['idade'] > media:
        print(f'{c["nome"]}', end=' ')