import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
V = [1.943, 1.545, 1.35, 0.841, 0.723]
ν = [8.21*10**14, 7.40*10**14, 6.44*10**14, 5.49*10**14, 5.19*10**14]

# Plotando os dados como pontos
plt.scatter(ν, V, color='b', label='Dados')  # Usando scatter para exibir apenas os pontos

plt.xlabel('Frequência (ν) [Hz]', fontsize=12, labelpad=12)  # Rótulo do eixo X
plt.ylabel('Voltagem (V) - Fundo de escala em [$10^{-13}$]', fontsize=12, labelpad=12)  # Rótulo do eixo Y
plt.title('Gráfico Voltagem de Parada x Frequência', fontsize=14)  # Título do gráfico

# Ajuste de uma linha de primeiro grau (linear)
coef = np.polyfit(ν, V, 1)
poly1d_fn = np.poly1d(coef)

# Plotando a linha de ajuste plt.plot(ν, poly1d_fn(ν), '--r', label=f'Linha de Ajuste (Coef Angular: {coef[2]:.2f})')   Adicionando o coeficiente angular à legenda, ajustar depois para o valor correto após verificar os dados certos da teoria #

plt.legend()  # Mostrar a legenda
plt.grid(True)  # Exibir as grades do gráfico

plt.show()  # Exibir o gráfico
