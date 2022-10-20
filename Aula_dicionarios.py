carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
valores = [88078.64, 106161.94, 72832.16, 124549.07]

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados, '\n')


dados = dict(zip(carros, valores))
print(dados, '\n')

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados['Passat'])

print('Passat' in dados)
print('Corsa' in dados)
print(len(dados), '\n')

dados['DS5'] = 124921.71
print(dados)

del dados['Passat']
print(dados)

dados.update({'Passat': 106161.94})
print(dados)

dados.update({'Passat': 106161.95, 'Fusca':150000})
print(dados)

dadosCopy = dados.copy()
print(dadosCopy)
del dadosCopy['Fusca']
print(dadosCopy)

print(dadosCopy.pop('Passat'))

print(dadosCopy.pop('Passat', 'Chave nao encontrada'))

dadosCopy.clear()
print(dadosCopy)
print('\n')

for key in dados.keys():
    print(dados[key])

print(dados.values())
print(dados.items())
print('\n')

for item in dados.items():
    print(item)
print('\n')
 
for key, value in dados.items():
    print(key, value)
print('\n')

for key, value in dados.items():
    if (value > 100000):
        print(key)
print('\n')