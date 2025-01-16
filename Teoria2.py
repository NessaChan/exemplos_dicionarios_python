brasil = []
estado1 = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['Uf'])
print(brasil[0]['Sigla'])
print(brasil[1]['Uf'])
print(brasil[1]['Sigla'])
print('-=' * 30)
estado = dict()
br = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    br.append(estado.copy())
print(br)
for e in br:
    for v in e.values():
        print(f'{v}', end=' ')
    print()

