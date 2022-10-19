#https://docs.python.org/3.6/library/stdtypes.html#typesmapping

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
print(nomes_carros)
print(type(nomes_carros))
print(nomes_carros[1:3], '\n')

for item in nomes_carros:
    print(item)
    
carro_1, carro_2, carro_3, carro_4 = nomes_carros

print('\n', carro_1,'\n', carro_2,'\n', carro_3, '\n', carro_4)
_, A, _, B = nomes_carros
print(A, B)

_, C, *_ = nomes_carros
print(C)

print('\n')
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
print(nomes_carros[-1][1], '\n')

carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
valores = [88078.64, 106161.94, 72832.16, 124549.07]

print(list(zip(carros, valores)))

for item in zip(carros, valores):
    print(item)
  
print('\n')  
for carro, valor in zip(carros, valores):
    print(carro, valor)
    
print('\n')  
for carro, valor in zip(carros, valores):
    if(valor > 100000):
        print(carro, '\n')
        

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