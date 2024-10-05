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


    df_empresas = pd.DataFrame()
    simbolos = []
    nombres = []
    cambios = []

    for gainer in gainers:

        simbolos.append(gainer['symbol'])
        nombres.append(gainer['name'])
        cambios.append(gainer['changesPercentage'])

        # df_empresas = pd.concat([df_empresas, pd.DataFrame.from_dict(empresas)])
        df_empresas = pd.DataFrame(list(zip(simbolos, nombres, cambios)),
               columns =['Ticker', 'Empresa', 'Cambio'])

    df_empresas.set_index('simbolos')
    # df_empresas.sort_values(by=['market_cap'], ascending=False, inplace=True)

    return df_empresas


def Calcular_e_imprimir_df(api_key):
    resultados = fetch_gainers(api_key)
    st.dataframe(resultados)
    


# Inicio del programa

api_key = 'BKewxsq6oAF5okFIZ5b84WGWGiy3kiOm'
Parametros_de_visualizacion()
Imprimir_pantalla()
Calcular_e_imprimir_df(api_key)


