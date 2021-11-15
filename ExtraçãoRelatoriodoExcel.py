import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


arquivo = 'Dados'

df_ex = pd.read_csv(arquivo,sheet_name = 'relatório')

df_ex.to_excel('relatorioFinal.xlsx')


print(df_ex['Broker'])

colunabroker = df_ex.grupby(['Broker']).median()

print(colunabroker)

relatorio = colunabroker.loc[:"Media":"Qty"]

print(relatorio)

relatorioplot(kind = 'bar')

plt.show()

