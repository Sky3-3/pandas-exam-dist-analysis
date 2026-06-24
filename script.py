```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Definición de semilla estática para garantizar la reproducibilidad del experimento
np.random.seed(1)

# Inicialización del lienzo estructurado (4 filas de gráficos independientes)
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 12))

# --- 1. Examen 1: Distribución Simétrica Unimodal con Outliers ---
plt.subplot(4, 1, 1)
mu, sigma = 80, 5
exam_1 = np.random.normal(mu, sigma, 120)
# Inyección manual de anomalías (valores atípicos aislados en la cola izquierda)
exam_1[50] = 55
exam_1[51] = 55
plt.hist(exam_1, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 1", fontsize=14)

# --- 2. Examen 2: Distribución Asimétrica Negativa (Sesgo a la Izquierda) ---
plt.subplot(4, 1, 2)
mu, sigma = 85, 5
exam_2_norm = np.random.normal(mu, sigma, 85)
exam_2_u = np.random.uniform(60, 80, 35)
exam_2 = np.concatenate((exam_2_norm, exam_2_u))
plt.hist(exam_2, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 2", fontsize=14)

# --- 3. Examen 3: Distribución Bimodal (Dos picos de frecuencia) ---
plt.subplot(4, 1, 3)
mu, sigma = 85, 5
exam_3_norm_1 = np.random.normal(mu, sigma, 70)
exam_3_norm_2 = np.random.normal(65, 3.5, 50)
exam_3 = np.concatenate((exam_3_norm_1, exam_3_norm_2))
plt.hist(exam_3, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 3", fontsize=14)

# --- 4. Examen Final: Distribución Normal Estándar de Control ---
plt.subplot(4, 1, 4)
mu, sigma = 80, 6
final_norm = np.random.normal(mu, sigma, 120)
final_exam = np.concatenate((final_norm, np.array([96, 96])))

print("Métricas del Examen Final:")
print("Media Aritmética: " + str(round(np.average(final_exam), 2)))
print("Mediana Central: " + str(round(np.median(final_exam), 2)))

plt.hist(final_exam, 25, range=[50, 100])
plt.xlabel("Score (%)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Final Exam", fontsize=14)

# Optimización de espaciados entre ejes de subtramas
fig.tight_layout()
plt.savefig("distribuciones_examenes.png")  # Exportación automática del gráfico
plt.close()
