# funções matemáticas
import math as m
# gera números aleatórios
import random

import pandas as pd
# estatística descritiva, plotagem de gráficos, etc
import statsmodels
# usado para arrays multidimensionais
import numpy as np
# organiza dados de forma tabular e anexar rótulos descritivos às linhas e colunas da tabela (séries temporais e bancos de dados enormes)
import pandas
import pandas_datareader as pdr
# biblioteca de gráficos 2D projetada para visualização de dados numpy
import matplotlib
import yfinance as yfin


def ferramentas_av():
    print(m.sqrt(16))

    # numpy array de n-dimensões = ndarray
    # ndarray é sempre homogênea
    a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

    print('variável a: ', a)

    print('shape do array: ', a.shape)
    print('posição do array[1,3]: ', a[1, 3])

    a[1, 2] = 8

    print('array novo: ', a)
    print("a[0]: ", a[0])
    print("a[1]: ", a[1])

    # random

    prob = random.random()
    print("probabilidade no random: ", prob)

    number = random.randint(1, 6)
    print("randint gerando número: ", number)
    matrix = np.random.randint(1, 6, (4, 6))
    print("matrix: ", matrix)

    ser = pd.Series(np.random.random(5), name="Column 01")

    print("série: ", ser)
    print("ser[2]: ", ser[2])

    #Leitura dados yahoo finance (método para funcionar a pesquisa do professor)
    yfin.pdr_override()

    ##Método da aula
    #pg = pdr.data.DataReader('PG', data_source='yahoo', start='1995-1-1')

    #Método atual
    pg = pdr.data.get_data_yahoo('PG', start='1995-1-1')

    print("Datareader PG: ")
    print(pg)

    print("PG info: ")
    print(pg.info())

    print("PG head: ")
    print(pg.head())
    print("PG tail: ")
    print(pg.tail())
    print("PG HEAD 200")
    print(pg.head(200))

    tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
    new_data = pd.DataFrame()
    for t in tickers:
        new_data[t] = pdr.data.get_data_yahoo(t,start='1995-1-1' )['Adj Close']

    print("new data tail()")
    print(new_data.tail())


if __name__ == '__main__':
    ferramentas_av()
