import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Nomes das planilhas dentro da arquivo

planilhas = ["Planilha1", "Planilha2", "Planilha3", "Planilha4", "Planilha5"]

# Listas das médias dos coeficientes e x

list_A_med = []
list_B_med = []
list_x = []

# Loop que lê todas as planilhas

for planilha in planilhas:
    df = pd.read_excel(r"tabela_otimizada_alterada.xlsx"r"", sheet_name=planilha)

    # Nomes das Colunas das planilhas

    times = ["T1", "T2", "T3", "T4", "T5"]
    position = ["X1", "X2", "X3", "X4", "X5"]

    # Listas para armazenar as somas necessarias para efetuar o calculo

    list_sum_x = []
    list_sum_t = []
    list_sum_xt = []
    list_sum_t2 = []
    N = []
    B = []
    A = []

    # Loop que conta quantos pares (x, t) em cada tabela e elimina celulas vazias

    for time in times:
        df[time] = df[time].dropna()
        n = df[time].count()
        N.append(n)

    for pos in position:
        df[pos] = df[pos].dropna()

    df = df.fillna(0)

    # Soma das posições (x)

    for pos in position:
        sum_x = df[pos].sum()
        list_sum_x.append(sum_x)

    # Soma da posição vezes o instante (x * t)

    for i in range(len(times)):
        t_x = df[times[i]] * df[position[i]]
        sum_t_x = sum(t_x)
        list_sum_xt.append(sum_t_x)

    # Somas do instante (t) e soma dos instante ao quadrado (t^2)

    for time in times:
        sum_t = df[time].sum()
        list_sum_t.append(sum_t)

        time_2 = df[time] ** 2
        sum_t2 = sum(time_2)
        list_sum_t2.append(sum_t2)

    # Loop que efetua os calculs dos coeficientes da equaçâo das retas

    for j in range(len(times)):
        b = (N[j] * list_sum_xt[j] - list_sum_t[j] * list_sum_x[j]) / (N[j] * list_sum_t2[j] - list_sum_t[j] ** 2)
        B.append(b)

        a = (list_sum_x[j] - B[j] * list_sum_t[j]) / N[j]
        A.append(a)

    # Calculo da Média dos coeficientes de cada reta

    A_Med = float(sum(A) / len(A))
    B_Med = float(sum(B) / len(B))

    t = np.linspace(0, 1)
    x = B_Med * t + A_Med
    list_x.append(x)

# Plotar gráfico

x0 = list_x[0]
x1 = list_x[1]
x2 = list_x[2]
x3 = list_x[3]
x4 = list_x[4]

plt.plot(t, x0, label='Esfera 1: Diâmetro = 0,680 cm', color='#1f77b4')
plt.plot(t, x1, label='Esfera 2: Diâmetro = 1,115 cm', color='#ff7f0e')
plt.plot(t, x2, label='Esfera 3: Diâmetro = 1,275 cm', color='#2ca02c')
plt.plot(t, x3, label='Esfera 4: Diâmetro = 1,750 cm', color='#d62728')
plt.plot(t, x4, label='Esfera 5: Diâmetro = 1,909 cm', color='#9467bd')

plt.legend()

plt.show()
