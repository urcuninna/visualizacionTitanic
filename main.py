import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Generar números aleatoreos
rng= np.random.RandomState(0) #Esta línea crea un generador de números aleatorios utilizando la función RandomState de NumPy, con una semilla específica (0). Al establecer una semilla, garantizamos que los números aleatorios generados serán los mismos cada vez que ejecutemos el código, lo que permite reproducir los resultados
print(rng)

#Esta línea utiliza la función linspace de NumPy para generar un array x de 500 puntos igualmente espaciados entre 0 y 10, incluidos ambos extremos.
x=np.linspace(0,10,500)

#rng.randn(500, 6)esta matriz tiene 500 filas y 6 columnas de valores aleatorios.np.cumsum(..., axis=0) Calcula la suma acumulativa de los elementos de la matriz generada, a lo largo del eje 0 (filas). Esto significa que para cada columna, el valor de cada fila es la suma de todos los valores anteriores en esa columna. Como resultado, Y tendrá el mismo tamaño que el array original (500x6), pero con valores acumulativos.
y=np.cumsum(rng.randn(500,6), axis=0)


plt.plot(x,y)
#La función legend añade una leyenda al gráfico actual, que sirve para identificar las diferentes curvas o series de datos representadas.Aquí, las letras 'A', 'B', 'C', 'D', 'E', 'F' serán las etiquetas asignadas a las curvas o series de datos en el orden en que fueron graficadas.Especifica el número de columnas en la leyenda. En este caso, ncol=2 significa que la leyenda tendrá 2 columnas.upper left' coloca la leyenda en la esquina superior izquierda del área del gráfico
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set()
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

#x**2 se utiliza intencionalmente para mostrar un comportamiento particular, en este caso, una función cuadrática.
y_val=x**2
plt.scatter(x,y_val, marker='s', color='g')
plt.title("Gráfico de dispersión")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()