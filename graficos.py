import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [10, 25, 15, 30]

# Criar o gráfico de barras
plt.bar(categorias, valores)

# Adicionar rótulos e título
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Exibir o gráfico
plt.show()