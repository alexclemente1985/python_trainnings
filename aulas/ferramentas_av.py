#funções matemáticas
import math as m
#gera números aleatórios
import random
#estatística descritiva, plotagem de gráficos, etc
import statsmodels
#usado para arrays multidimensionais
import numpy as np
#organiza dados de forma tabular e anexar rótulos descritivos às linhas e colunas da tabela (séries temporais e bancos de dados enormes)
import pandas
import pandas_datareader
#biblioteca de gráficos 2D projetada para visualização de dados numpy
import matplotlib
def ferramentas_av():
    print(m.sqrt(16))

    #numpy array de n-dimensões = ndarray
    #ndarray é sempre homogênea
    a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

    print('variável a: ', a)



if __name__ == '__main__':
    ferramentas_av()