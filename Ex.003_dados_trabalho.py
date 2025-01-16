'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
 em um dicionario, se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano
de contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa 
vai se aposentar.'''
from datetime import datetime
trabalhador = dict()
trabalhador['Nome:'] = str(input('Nome:'))
anonasc = int(input('Ano de nascimento: '))
trabalhador['CTPS'] = int(input('Nº da carteira de trabalho:(se não tiver, digite 0): '))
trabalhador['Idade'] = datetime.now().year - anonasc
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input('Ano que foi contratato: '))
    trabalhador['Salário'] = float(input('Salário: '))
    trabalhador['Ano de aposentadoria'] = trabalhador['Ano de contratação'] + 35
    trabalhador['Idade da aposentadoria'] = trabalhador['Ano de aposentadoria'] -anonasc
print('-=' * 30)
for k, v in trabalhador.items():
    if trabalhador['CTPS'] == 0:
        trabalhador['CTPS'] = 'Não tem'
    print(f'{k} = {v}')
