import numpy as np
from matplotlib import pyplot as plt # Importar o módulo especifico pyplot do matplotlib

array_user = np.linspace(0,5,100)

# array_yser -> eixo x
# array_user -> eixo y

plt.plot(array_user,array_user, label = 'linear') # Legenda especificada na função plot

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico simples')
plt.legend()
plt.savefig('exp.png')
plt.show()
