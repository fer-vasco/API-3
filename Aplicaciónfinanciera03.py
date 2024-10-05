import requests
import pandas as pd
import streamlit as st
from datetime import datetime


def Parametros_de_visualizacion():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)


def Imprimir_pantalla():
    corrida = datetime.now()
    corrida = corrida.strftime('%m-%d-%y %H:%M')

    st.title('Resultados')
    st.write(f'Datos actualizados el {corrida}')


def market_cap(ticker, api_key):
    url = f'https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={api_key}'
    response = requests.get(url)
    resultado = response.json()
    
    return resultado[0]['marketCap']


def fetch_gainers(api_key):
    url = f'https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={api_key}'
    response = requests.get(url)
    gainers = response.json()

    empresas = {
        'symbol':'',
        'name':'',
        'changesPercentage':''
        }


    df_empresas = pd.DataFrame()

    for gainer in gainers:

        '''
        empresas = {
            'symbol':[gainer['symbol']],
            'name':[gainer['name']],
            'changesPercentage':[gainer['changesPercentage']],
            'market_cap':[market_cap(gainer['symbol'], api_key)]
            }'''

        empresas = {
            'symbol':[gainer['symbol']],
            'name':[gainer['name']],
            'changesPercentage':[gainer['changesPercentage']]
            }

        df_empresas = pd.concat([df_empresas, pd.DataFrame.from_dict(empresas)])
        
                
    # df_empresas.sort_values(by=['market_cap'], ascending=False, inplace=True)

    return df_empresas


def Calcular_e_imprimir_df(api_key):
    resultados = fetch_gainers(api_key)
    st.dataframe(resultados)




# Inicio del programa
# -------------------

api_key = 'BKewxsq6oAF5okFIZ5b84WGWGiy3kiOm'
Parametros_de_visualizacion()
Imprimir_pantalla()
Calcular_e_imprimir_df(api_key)


