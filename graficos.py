import pandas as pd
import plotly.express as px

# Carregar o arquivo CSV
file_path = 'cases-brazil-total.csv'
data = pd.read_csv(file_path)

# Remover a linha total para focar nos estados individuamente
data_states = data[data['state'] != 'TOTAL']

# Renomear colunas para português
data_states = data_states.rename(columns={
    'totalCases': 'Casos Totais',
    'deaths': 'Mortes Totais',
    'totalCases_per_100k_inhabitants': 'Casos Totais por 100k Habitantes',
    'deaths_per_100k_inhabitants': 'Mortes por 100k Habitantes'
})

# 1. Gráfico de Pizza: Distribuição dos casos totais entre os estados
fig_pie = px.pie(data_states, values='Casos Totais', names='state', title='Distribuição dos Casos Totais de COVID-19 nos Estados Brasileiros',
                 labels={'Casos Totais': 'Casos Totais', 'state': 'Estado'})
fig_pie.show()

# 2. Gráfico de Barras: Casos totais vs. Mortes totais
fig_bar = px.bar(data_states, x='state', y=['Casos Totais', 'Mortes Totais'], title='Casos Totais vs. Mortes Totais nos Estados Brasileiros',
                 labels={'state': 'Estado', 'value': 'Total', 'variable': 'Métrica'},
                 barmode='group')
fig_bar.show()

# 3. Dados para o gráfico de linha
data_line = data_states.melt(id_vars='state', value_vars=['Casos Totais por 100k Habitantes', 'Mortes por 100k Habitantes'],
                             var_name='Métrica', value_name='Valor')

# Gráfico de Linha: Casos totais por 100k habitantes vs. Mortes por 100k habitantes
fig_line = px.line(data_line, x='state', y='Valor', color='Métrica', title='Casos Totais por 100k Habitantes vs. Mortes por 100k Habitantes',
                   labels={'state': 'Estado', 'Valor': 'Valor', 'Métrica': 'Métrica'})
fig_line.show()
