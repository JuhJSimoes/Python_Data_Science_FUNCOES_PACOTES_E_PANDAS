import sys
import pandas as pd
#pd.set_option('display.max_rows', 100)
#pd.set_option('display.max_rows', 3)

dataset = pd.read_csv('../Python_Data_Science_FUNCOES_PACOTES_E_PANDAS/Pandas/data/db.csv', sep=';')
print(dataset, '\n')

print(dataset[['Quilometragem', 'Valor']].describe(), '\n')

print(dataset.info(), '\n')


