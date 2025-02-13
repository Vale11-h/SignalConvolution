# Convolución, correlación y transformación
## Introducción

En este laboratorio se exploran conceptos fundamentales del procesamiento de señales a través de la aplicación de operaciones como la convolución, correlación y el análisis estadístico de la señal. Se utilizaron tanto métodos manuales como herramientas computacionales (Python, Colab) para llevar a cabo los cálculos y visualizaciones necesarias.

Inicialmente, se trabajó con la operación de convolución en sistemas discretos. Para ello, se definió una respuesta al impulso 
*h[n]* a partir de los dígitos del código estudiantil y una señal de entrada *x[n]* utilizando los dígitos de la cédula. Dado que el grupo está conformado por tres estudiantes, se realizaron tres convoluciones independientes. Estas se desarrollaron paso a paso utilizando sumatorias manuales y luego se verificaron los resultados implementando el procedimiento en Python. 

Luego, se abordó la correlación entre dos señales: una cosenoidal y otra senoidal, ambas con frecuencia de 100 Hz y un tiempo de muestreo de 1.25 ms. El cálculo de la correlación permitió identificar similitudes entre las señales y evaluar su comportamiento temporal. 

Finalmente, se trabajó con una señal electroencefalográfica (EEG) descargada de la base de datos PhysioNet. Esta señal fue caracterizada en el dominio del tiempo mediante el cálculo de estadísticos descriptivos, como la media, mediana, desviación estándar y el análisis de su histograma. Además, se aplicó la transformada de Fourier para observar su comportamiento en el dominio de la frecuencia junto con la estimación de su densidad espectral.

## Análisis

### Convolución.

La convolución es una operación que permite determinar cómo una señal de entrada *x[n]* se transforma al pasar por un sistema descrito por su respuesta al impulso *h[n]*. Consiste en desplazar, multiplicar y sumar los valores de ambas señales, lo que da como resultado la señal de salida *y[n]*.  

A continuación, se presentan las tres convoluciones realizadas correspondientes a los datos de cada integrante del grupo, comparando los resultados realizados a mano con los obtenidos en Python.

![a](https://github.com/user-attachments/assets/2c90c075-dca3-4d84-8ab9-24c93522d03b)
>*Señal Y[n] 1 resultante, cálculo manual.*

![aa](https://github.com/user-attachments/assets/b18725b7-a3c5-471f-9e33-67a8238feb0e)
>*Señal Y[n] 1 resultante, cálculo en Python.*

<p align="center">
  <img src="https://github.com/user-attachments/assets/e361f975-9ddc-4b03-a744-d4f65871e5da" alt="aaaaa" width="45%"/>
  <img src="https://github.com/user-attachments/assets/67194e7e-97ef-4c73-89bd-d4e8e62489b1" alt="aaaa" width="45%"/>
</p>

>*Gráfica de convolución 1, manual y en Python.*

![b](https://github.com/user-attachments/assets/1e3fc8b0-63cb-45af-a9ff-1414db66d659)
![bbbb](https://github.com/user-attachments/assets/39af9142-d863-4e5a-b429-fae6ed03f496)
>*Señal Y[n] 2 resultante, cálculo manual.*

![bb](https://github.com/user-attachments/assets/0d2c8460-0a7f-4b32-9562-7a92ace5e561)
>*Señal Y[n] 2 resultante, cálculo en Python.*

<p align="center">
  <img src="https://github.com/user-attachments/assets/b0251529-30e8-42c8-a6ae-21ac662b4393" alt="bbbbb" width="45%"/>
  <img src="https://github.com/user-attachments/assets/ae879e79-ced1-48ea-a659-c3202b038a8d" alt="bbbbbb" width="45%"/>
</p>

>*Gráfica de convolución 2, manual y en Python.*

![c](https://github.com/user-attachments/assets/ea1e8910-fca1-4a96-b3ba-bdb86d36e2ec)
>*Señal Y[n] 3 resultante, cálculo manual.*

![cc](https://github.com/user-attachments/assets/a9e9e8f4-c349-4f36-842f-4849c0ee23d1)
>*Señal Y[n] 3 resultante, cálculo en Python.*

<p align="center">
  <img src="https://github.com/user-attachments/assets/73da0916-e9e2-494d-94f8-40a4c5738552" alt="c1" width="45%"/>
  <img src="https://github.com/user-attachments/assets/fa76312a-bc97-4b5e-8e4a-828c32859e0a" alt="c2" width="45%"/>
</p>

>*Gráfica de convolución 3, manual y en Python.*

### Correlación.

La correlación es una operación que permite medir el grado de similitud entre dos señales a lo largo del tiempo. Al comparar *x₁[n]* y *x₂[n]*, se identifica si presentan patrones similares, si están desfasadas o si no guardan relación.

En este procedimiento, se calculó la correlación entre las señales:

- *x₁[n]* = cos(2π100nTₛ)  
- *x₂[n]* = sin(2π100nTₛ)  

para Tₛ = 1.25 ms.

![d](https://github.com/user-attachments/assets/0d7d994a-3ea0-4af2-b303-8af925051d07)

>*Gráfica de correlación.*

La gráfica obtenida muestra picos positivos y negativos, lo que indica momentos de alineación o desfase entre las señales:

     • Picos positivos: (Como el de 3.5 ) Muestran que las señales coinciden mejor cuando una se desplaza cierta cantidad.
     • Picos negativos: (Como el de -3.5) Muestran que las señales están "desfasadas" o no coinciden.

Los valores positivos y negativos parecen alternarse, lo que es normal cuando comparamos una señal de coseno con una de seno, ya que siempre están desfasadas 90°, además se observa que la correlación pasa varias veces por el cero, lo que significa que, en esos desplazamientos específicos, las señales no tienen una relación clara ni positiva ni negativa.
