import pandas as pd
from twilio.rest import Client
import requests
# ---------------------------------------------------------------------------

# API´S de integração para o desenvolvimento do sistema

# Pandas

# openpyxl

# twilio

# --------------------------------------------------------------------------

# passo a passo de solução

# Abrir os 6 arquivos de Vendas em excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Número de Vendas: {vendas}')

account_sid = "AC1cc6aae4e4650e22e2ec22f18682716b"
auth_token  = "8c41bce00a9b031e39480750acbc275b"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5519981224006",
    from_="+12705617501",
    body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Número de Vendas: {vendas}')

print(message.sid)


        

# Para cada arquivo devemos:

# Verificar se algum valor a coluna Vendas daquele arquivo é maior que 55.000

# se for maior do que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor

# caso seja menor do que 55.000 -> Não fazer nada

# ------------------------------------------------------------------------

# _fUuKWCUDn9BHjBcXljc2yfL1E5h7JxvQkVqTZnS