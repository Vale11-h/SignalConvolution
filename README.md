# Convolución, correlación y transformación
## Introducción

En este laboratorio se exploran conceptos fundamentales del procesamiento de señales a través de la aplicación de operaciones como la convolución, correlación y el análisis estadístico de la señal. Se utilizaron tanto métodos manuales como herramientas computacionales (Python, Colab) para llevar a cabo los cálculos y visualizaciones necesarias.

Inicialmente, se trabajó con la operación de convolución en sistemas discretos. Para ello, se definió una respuesta al impulso 
*h[n]* a partir de los dígitos del código estudiantil y una señal de entrada *x[n]* utilizando los dígitos de la cédula. Dado que el grupo está conformado por tres estudiantes, se realizaron tres convoluciones independientes. Estas se desarrollaron paso a paso utilizando sumatorias manuales y luego se verificaron los resultados implementando el procedimiento en Python. 

Luego, se abordó la correlación entre dos señales: una cosenoidal y otra senoidal, ambas con frecuencia de 100 Hz y un tiempo de muestreo de 1.25 ms. El cálculo de la correlación permitió identificar similitudes entre las señales y evaluar su comportamiento temporal. 

Finalmente, se trabajó con una señal electroencefalográfica (EEG) descargada de la base de datos PhysioNet. Esta señal fue caracterizada en el dominio del tiempo mediante el cálculo de estadísticos descriptivos, como la media, mediana, desviación estándar y el análisis de su histograma. Además, se aplicó la transformada de Fourier para observar su comportamiento en el dominio de la frecuencia junto con la estimación de su densidad espectral.

## Análisis

### Convolución.

[^1^] La convolución es una operación que permite determinar cómo una señal de entrada *x[n]* se transforma al pasar por un sistema descrito por su respuesta al impulso *h[n]*. Consiste en desplazar, multiplicar y sumar los valores de ambas señales, lo que da como resultado la señal de salida *y[n]*. 

[^1^]: BARGETZ, CHRISTIAN. Convolution of Distribution-Valued Functions. Applications. Rev.colomb.mat. [online]. 2011, vol.45, n.1 [cited  2025-02-13], pp.51-80. Available from: <http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0034-74262011000100005&lng=en&nrm=iso>. ISSN 0034-7426.
Electronic Document Format(ABNT)

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

[^2^] La correlación es una operación que permite medir el grado de similitud entre dos señales a lo largo del tiempo. Al comparar *x₁[n]* y *x₂[n]*, se identifica si presentan patrones similares, si están desfasadas o si no guardan relación.
[^2^]: Zar, J. 1999. Biostatistical Analysis. 4th Ed. Prentice Hall, New Jersey.

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

### Análisis de la señal.

Para este análisis, se extrajo una señal de electroencefalografía (EEG) de la base de datos PhysioNet, que registra la actividad eléctrica cerebral mediante electrodos en el cuero cabelludo. La señal presenta los siguientes canales disponibles, que corresponden a diferentes ubicaciones del cerebro, permitiendo registrar la actividad de diversas regiones.

- Canales EEG: Fp1, Fp2, F3, F4, F7, F8, T3, T4, C3, C4, T5, T6, P3, P4, O1, O2, Fz, Cz, Pz, A2-A1.
  
![e](https://github.com/user-attachments/assets/3c5de83b-da40-4e44-98d6-1f02c289553a)
>*Señal EEG.*

La frecuencia de muestreo de la señal es de **500 Hz**, lo que significa que se capturan **500 muestras por segundo**, permitiendo un análisis detallado de las oscilaciones neuronales.

#### Estadísticos Descriptivos.

     •  Media:4.89 × 10⁻⁸  Indica que la señal oscila alrededor del cero, lo que es esperado en EEG.
     •  Desviación estándar: 9.19 × 10⁻⁶  Muestra poca variabilidad, lo que sugiere una señal estable.
     •  Valor máximo: 5.94 × 10⁻⁵  Amplitud máxima detectada.
     •  Valor mínimo: -4.52 × 10⁻⁵  Amplitud mínima registrada.

#### Clasificación de la Señal EEG (Canal Fp1).

   - **Analógica** en su origen, ya que la actividad eléctrica del cerebro es continua.  
   - **Digitalizada**, pues se ha muestreado a 500 Hz para su análisis en el computador.    
   - **Temporal**, ya que su variación se observa en función del tiempo.  
   - **No periódica**, debido a que la actividad cerebral es irregular y no se repite de manera predecible.    
   - **Discreta**, porque se midió en ciertos puntos específicos del tiempo, no de manera continua, es decir se toma un valor cada 2 milisegundos (500 veces por segundo). 

#### Transformada de Fourier y densidad espectral.

![eee](https://github.com/user-attachments/assets/93885e03-c015-463f-907c-89e45a119645)
>*TF de la señal EEG.*

[^3^]  La Transformada de Fourier (TF) se utiliza para analizar una señal en el dominio de la frecuencia. En la gráfica obtenida, se observa que la mayor parte de la energía se concentra en frecuencias menores a 40 Hz, lo cual es característico de las ondas cerebrales asociadas a estados de reposo, atención y sueño. Los picos evidencian las frecuencias dominantes, lo que facilita la interpretación de la actividad cerebral subyacente.

[^3^]:Coordinación de Ciencias Aplicadas (2019). Programa de estudio matemáticas avanzadas. DCB, FI, UNAM. Recuperado el 17 de junio de 2022, de https://dcb.ingenieria.unam.mx/wp-content/themes/temperachild/CoordinacionesAcademicas/CA/MA/Documentos/Programa2016.pd

 ![f](https://github.com/user-attachments/assets/e9721bb8-2cf3-4893-8419-b2f2e121f2f6)
>*PSD de la señal EEG.*

La Densidad Espectral de Potencia (PSD) permite analizar cómo se distribuye la potencia de la señal EEG en el dominio de la frecuencia. En la gráfica obtenida se observa que las mayores concentraciones de potencia se encuentran en las frecuencias más bajas, con picos significativos alrededor de 2 Hz con un valor aproximado de 2.5 × 10⁻⁸, 5 Hz con 3.0 × 10⁻⁸, siendo este el máximo registrado, y 10 Hz con 1.0 × 10⁻⁸. 

Estos picos corresponden a las bandas de frecuencia asociadas a las ondas delta y theta, que suelen aparecer en estados de relajación o descanso. 

#### Estadísticos descriptivos en función de la frecuencia.

![g](https://github.com/user-attachments/assets/8a92a7da-73ac-42a7-884a-ad5bafef9129)
>*Estadísticos descriptivos en función de la frecuencia.*

     • Frecuencia media: 8.73 Hz, lo que indica que la señal EEG tiene una mayor concentración de energía en las frecuencias bajas, correspondientes a las bandas delta y theta.
     • Frecuencia mediana: 10.74 Hz, lo que significa que el 50% de la potencia de la señal se encuentra en frecuencias inferiores a este valor, sugiriendo una actividad predominante en el rango de las ondas alfa.
     • Desviación estándar: 7.02 Hz, lo que refleja una dispersión moderada de las frecuencias alrededor de la media, lo que es característico de señales EEG en reposo.
     • Histograma de frecuencias: El histograma muestra una mayor densidad espectral acumulada en las frecuencias más bajas, con una disminución progresiva a medida que aumenta la frecuencia, lo que concuerda con la actividad cerebral típica en estados de relajación.
     
## Instrucciones

**1. Convolución y correlación.**

• Se aplicaron las operaciones de convolución y correlación a señales específicas para analizar su comportamiento, identificar similitudes y comprender la relación entre ellas.

###### Para ello, se utilizaron las funciones np.convolve() y np.correlate() de la librería numpy, aplicándolas a las señales dadas y graficando los resultados con matplotlib.pyplot.

**2. Análisis de la señal EEG.**

• Se extrajo una señal EEG del conjunto de datos proporcionado en PhysioNet utilizando la función wfdb.rdrecord().
• Se trabajó con uno de los canales disponibles y se almacenaron sus datos en un arreglo para su posterior análisis.

###### Se calcularon las estadísticas descriptivas: media, mediana, desviación estándar, valor máximo y mínimo, utilizando las funciones np.mean(), np.median(), np.std(), np.max() y np.min().

• Se determinó la frecuencia de muestreo de la señal (500 Hz), lo que permite capturar 500 muestras por segundo.

###### Se aplicó la Transformada de Fourier para visualizar las componentes de frecuencia presentes en la señal, empleando np.fft.fft() y np.fft.fftfreq().

• Se calculó la densidad espectral de potencia (PSD) con la función scipy.signal.welch() para conocer la distribución de la energía en las distintas frecuencias.

**3. Análisis en función de la frecuencia.**

• Se calcularon las estadísticas descriptivas relacionadas con la frecuencia: media, mediana, desviación estándar y distribución espectral.

###### Utilizando np.mean(), np.median(), np.std().

• Se construyó un histograma de frecuencias para observar cómo se distribuyen las componentes frecuenciales, utilizando plt.hist().

**4. Herramientas utilizadas.**

• Python en Google Colab, utilizando las librerías numpy, matplotlib y scipy para el procesamiento y análisis de la señal.

## Requisitos

• Tener Python 3.9 instalado y utilizar Google Colab (o cualquier compilador compatible).

• Tener acceso al archivo .edf para cargar en Google Colab o el compilador elegido.

• Contar con las librerías necesarias instaladas para ejecutar el código correctamente (especificadas en el inicio del artículo).

## Usar

Por favor, cite este artículo:

Huertas, V.; Ramírez, P.; Delgado, A. Análisis estadístico de la señal. 13 de febrero de 2025.

## Información de contacto

• est.laurav.huertas@unimilitar.edu.co
• est.deisy.aramirez@unimilitar.edu.co
• est.paulav.gomez@unimilitar.edu.co

## Anexo: Ondas Cerebrales

El análisis de la señal EEG implicó el cálculo de diversas variables, como estadísticas descriptivas, Transformada de Fourier y densidad espectral de potencia, las cuales permiten comprender la presencia y distribución de las distintas ondas cerebrales. A continuación, se incluye una imagen que ilustra las principales ondas y sus rangos de frecuencia para contextualizar el estudio realizado.

![h](https://github.com/user-attachments/assets/203bde06-833f-4b37-ad26-58af5ea8cbcf)
>*Ondas cerebrales.*
