import sys
import pandas as pd
#https://pandas.pydata.org/pandas-docs/version/0.25/
#https://pandas.pydata.org/pandas-docs/stable/
#https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html


#pd.set_option('display.max_rows', 100)
#pd.set_option('display.max_rows', 3)


dataset = pd.read_csv('../Python_Data_Science_FUNCOES_PACOTES_E_PANDAS/Pandas/data/db.csv', sep=';')
print(dataset, '\n')

print(dataset[['Quilometragem', 'Valor']].describe(), '\n')

print(dataset.info(), '\n')

carros = ['Jetta Variant', 'Passat', 'Crossfox']
print(pd.Series(carros), '\n')


dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)

dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Zero_km', 'Valor']] #altera a ordem das colunas

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

dataset = pd.DataFrame(dados)
print(dataset, '\n')


dataset = pd.read_csv('../Python_Data_Science_FUNCOES_PACOTES_E_PANDAS/Pandas/data/db.csv', sep=';', index_col = 0)
print(dataset, '\n')

dataset.head()

print(type(dataset[['Valor']]))# 2 colchetes altera de Series para Dataframe

print(dataset[0:3])

print(dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']], '\n')#loc faz seleções
print(dataset.loc[:, ['Motor', 'Valor']], '\n')


print(dataset.iloc[[1]]) #iloc seleciona baseado em numerico
print(dataset.iloc[1:4])
print(dataset.iloc[1:4, [0, 5, 2]])
print(dataset.iloc[[1,42,22] , [0, 5, 2]], '\n')

print('\n')

#Queries com DataFrames

dataset.head()
print(dataset.Motor)
select = dataset.Motor == 'Motor Diesel'
print(dataset[select])
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)], '\n')
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))


for item in dataset:
    print(item)
    
for index, row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = row['Quilometragem']/(2019 - row['Ano'])
    else:
        dataset.loc[index, 'Km_media'] = 0
        
print(dataset, '\n')

print(dataset.Quilometragem.isna())

print(dataset[dataset.Quilometragem.isna()])

dataset.fillna(0, inplace=True) #sem o inplace=True a alteração é apenas visual, necessario esse parametro para salvar no dataset.
print(dataset)

print(dataset.query('Zero_km == True'))
print('\n')

dataset = pd.read_csv('../Python_Data_Science_FUNCOES_PACOTES_E_PANDAS/Pandas/data/db.csv', sep=';')

dataset.dropna(subset=['Quilometragem'], inplace=True)
print(dataset)

