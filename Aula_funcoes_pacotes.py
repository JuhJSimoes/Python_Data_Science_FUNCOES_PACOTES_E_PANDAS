#https://docs.python.org/3.6/library/functions.html

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

valores = []
for valor in dados.values():
    valores.append(valor)
print(valores, '\n')

soma = 0
for valor in dados.values():
    soma += valor
print(soma, '\n')

list(dados.values())
print(dados)

print(sum(dados.values()))
#print(sum(dados.values(),5000))
print('\n')

'''def <nome>():
    <instruções>'''
    
def media():
    valor = (1 + 2 + 3)/3
    print(valor)
    
media()

def media(number_1, number_2, number_3):
    valor = (number_1 + number_2 + number_3)/3
    print(valor)
    
media(23, 45, 67)
print('\n')

def media(lista):
    valor = sum(lista)/len(lista)
    print(valor)

media([50, 10000, 33, 15, 8])
print('\n')

def media(lista):
    valor = sum(lista)/len(lista)
    return valor

resultado = media([50, 10000, 33, 15, 8])
print(resultado, '\n')

def media(lista):
    valor = sum(lista)/len(lista)
    return (valor, len(lista))

resultado, n = media([50, 10000, 33, 15, 8])
print(resultado)
print(n)



