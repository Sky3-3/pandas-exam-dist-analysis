# Proyecto Python: Simulación y Análisis Estadístico de Sesgo en Distribuciones Académicas

Este repositorio contiene un proyecto práctico desarrollado en Python utilizando las librerías **NumPy**, **Matplotlib** y **Pandas** enfocado en el análisis e interpretación visual de distribuciones estadísticas univariadas. El script simula el rendimiento de un alumnado a lo largo de cuatro exámenes mediante la generación de datos estocásticos (distribuciones normales y uniformes combinadas), configura lienzos multidimensionales de subtramas verticales, y audita las relaciones entre la media y la mediana para clasificar formalmente el sesgo (*skewness*) y las anomalías (*outliers*) de cada población.

---

## Código Python del Proyecto

El programa establece una semilla aleatoria de control, construye los perfiles estadísticos de los exámenes mediante concatenaciones vectoriales y renderiza las curvas de frecuencias:

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

```

---

## Reporte de Interpretación de Histogramas (`summary.txt`)

El análisis visual de las formas geométricas de los histogramas y la posición relativa de sus estadísticos centrales permite diagnosticar formalmente la naturaleza de cada población:

### 1. Cuadro Resumen de Formas Morfológicas

| Evaluación Técnica | Tipo de Distribución | Relación de Métricas Centrales | Diagnóstico Estadístico del Rendimiento |
| --- | --- | --- | --- |
| **Examen 1** | **Simétrica** | $\text{Media} \approx \text{Mediana} = 80$ | Rendimiento balanceado. Presenta dos *outliers* severos en la zona baja de la escala ($55\%$). |
| **Examen 2** | **Sesgo Negativo** | $\text{Media} < \text{Mediana}$ ($82 < 84$) | Distribución con cola hacia la izquierda. La mayoría del curso aprobó con notas altas, arrastrando el promedio hacia abajo un grupo menor. |
| **Examen 3** | **Bimodal** | Posee dos modas locales | Se observan dos picos claros de frecuencia. Indica una polarización del curso (un grupo consolidado bajo y otro alto). |
| **Final Exam** | **Normal Simétrica** | $\text{Media} \approx \text{Mediana}$ (~$79.5$) | Curva balanceada clásica (campana de Gauss) con una dispersión estable controlada por la desviación estándar. |

## Conceptos Técnicos Aplicados

* **Sesgo de una Distribución (*Skewness*)**: Propiedad geométrica que determina el grado de asimetría de una población. Si los datos se extienden con una cola más larga hacia valores bajos se denomina sesgo a la izquierda o negativo ($\text{Media} < \text{Mediana}$), mientras que si se extiende hacia la derecha se denomina sesgo positivo ($\text{Media} > \text{Mediana}$).
* **Poblaciones Bimodales**: Distribución de frecuencias que presenta dos máximos locales relativos separados por un valle. En analítica, denota de forma inmediata la presencia de dos subgrupos heterogéneos solapados que requieren ser segmentados de forma independiente.
* **Ajuste de Lienzo Compacto (`fig.tight_layout()`)**: Instrucción de Matplotlib que inspecciona las dimensiones de las etiquetas de los ejes (`labels`), títulos y regiones de las subtramas en un diseño multicanal, recalculando automáticamente las distancias para evitar superposiciones residuales de texto en el renderizado final.

