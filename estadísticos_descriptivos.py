# -*- coding: utf-8 -*-
"""Estadísticos descriptivos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XN0DR_3aQt-FoE3_OGlpORNIcnNXUfXY
"""

!pip install mne

import mne
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Subir el archivo .edf desde la computadora
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
raw = mne.io.read_raw_edf(file_name, preload=True)

# Obtener los nombres de los canales
channel_names = raw.ch_names
print(f"Canales disponibles: {channel_names}")

# Obtener la frecuencia de muestreo
fs = raw.info['sfreq']
print(f"Frecuencia de muestreo: {fs} Hz")

# Seleccionar el primer canal (puedes cambiarlo según el archivo)
señal, tiempos = raw[:1]  # Extraer el primer canal de la señal

# Aplanar la señal (en caso de que tenga más de una dimensión)
señal = señal[0]

# Graficar la señal en función del tiempo
plt.figure(figsize=(10, 4))
plt.plot(tiempos, señal, color='magenta', label="Señal EDF")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (v)")
plt.title(f"Señal del canal {channel_names[0]}")
plt.legend()
plt.grid()
plt.show()

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(f"Media: {np.mean(señal)}")
print(f"Desviación estándar: {np.std(señal)}")
print(f"Máximo: {np.max(señal)}")
print(f"Mínimo: {np.min(señal)}")

# ----------------- TRANSFORMADA DE FOURIER -----------------
N = len(señal)  # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/fs)  # Vector de frecuencias
fft_values = np.fft.fft(señal)  # Aplicar FFT
fft_magnitude = np.abs(fft_values)  # Magnitud de la FFT

# Graficar la transformada de Fourier
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N // 2], fft_magnitude[:N // 2], color='purple')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("Transformada de Fourier de la señal")
plt.grid()
plt.show()

# ----------------- DENSIDAD ESPECTRAL DE POTENCIA -----------------
psd = (fft_magnitude ** 2) / N  # Densidad espectral de potencia

# Graficar la densidad espectral de potencia
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N // 2], psd[:N // 2], color='purple')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral de potencia")
plt.title("Densidad espectral de potencia (PSD)")
plt.grid()
plt.show()

# ----------------- ESTADÍSTICOS EN FUNCIÓN DE LA FRECUENCIA -----------------
# Frecuencia media
freq_mean = np.sum(frequencies[:N // 2] * psd[:N // 2]) / np.sum(psd[:N // 2])
print(f"\nFrecuencia media: {freq_mean:.2f} Hz")

# Frecuencia mediana
sorted_freqs = frequencies[:N // 2][np.argsort(psd[:N // 2])]
cumulative_power = np.cumsum(np.sort(psd[:N // 2]))
median_index = np.where(cumulative_power >= np.sum(psd[:N // 2]) / 2)[0][0]
freq_median = sorted_freqs[median_index]
print(f"Frecuencia mediana: {freq_median:.2f} Hz")

# Desviación estándar de la frecuencia
freq_std = np.sqrt(np.sum(psd[:N // 2] * (frequencies[:N // 2] - freq_mean) ** 2) / np.sum(psd[:N // 2]))
print(f"Desviación estándar de la frecuencia: {freq_std:.2f} Hz")

# ----------------- HISTOGRAMA DE FRECUENCIAS -----------------
plt.figure(figsize=(10, 4))
plt.hist(frequencies[:N // 2], bins=30, weights=psd[:N // 2], color='pink')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral acumulada")
plt.title("Histograma de la distribución de frecuencias")
plt.grid()
plt.show()