# Make sure you have some data

import pandas as pd
from matplotlib import pyplot as plt

import plot_likert

# Ler os dados da planilha XLSX
df = pd.read_excel('Questionário de Atitudes em relação à Robótica.xlsx', sheet_name='Ordenados por categoria')
# Selecionar as colunas a partir da coluna 9 até a penúltima coluna
# Preencher colunas vazias com um valor específico (por exemplo, "Neutro")

# Substituir os valores numéricos pelos valores de texto correspondentes


#df_fill = df.iloc[:, 5:].replace({1: 'Discordo Totalmente', 2: 'Discordo Parcialmente', 3: 'Concordo Parcialmente', 4: 'Concordo Totalmente'})
# Atualizar o DataFrame com as colunas preenchidas
#pg = df.iloc[:, 5:] = df_filled
#print(pg)


perguntas = df.iloc[:, 5:-1].fillna("Neutro")

print(perguntas)


# commit



likert_plot = plot_likert.plot_likert(perguntas, plot_likert.scales.agree5, plot_percentage=True)


# Ajustar o tamanho da figura
fig = likert_plot.get_figure()
fig.set_size_inches(35.5, 22.8)  # Defina as dimensões desejadas (largura, altura) em polegadas



# Exibir o gráfico
plt.title("Questionário de Atitudes em relação à Robótica")
plt.show()
