# Proyecto Python: Análisis Descriptivo e Interpretación de Distribuciones Académicas

Este repositorio contiene un proyecto práctico enfocado en la auditoría estadística e interpretación analítica de distribuciones de frecuencias univariadas. El objetivo de este análisis es evaluar el comportamiento del rendimiento de una cohorte estudiantil a lo largo de cuatro evaluaciones consecutivas, diagnosticando de forma teórica y visual las propiedades de forma (simetría, asimetría y multimodalidad), las métricas de dispersión (rango absoluto) y la presencia de anomalías o valores atípicos (*outliers*) sobre histogramas de densidad.

---

## Estructura del Análisis Estadístico (Archivo summary.txt)

A continuación se detalla la documentación técnica formal que describe la morfología matemática de cada una de las pruebas evaluadas:

### 1. Examen 1: Distribución Simétrica Unimodal
* **Métricas Centrales:** Media aritmética de $80\%$ y Mediana de $80\%$.
* **Morfología de la Forma:** Al ser la media exactamente igual a la mediana, la distribución se define como **perfectamente simétrica**. Los puntajes se distribuyen uniformemente con la misma densidad tanto a la izquierda como a la derecha del centro de masas.
* **Dispersión y Anomalías:** El rango absoluto es cercano a $35$ puntos, extendiéndose desde una nota mínima próxima a $55$ hasta una máxima de $90$. Se detecta **un valor atípico (*outlier*)** en el extremo inferior izquierdo, correspondiente al estudiante que obtuvo una calificación cercana a $55$.

### 2. Examen 2: Distribución Asimétrica a la Izquierda (*Left-Skewed*)
* **Métricas Centrales:** Media aritmética de $82\%$ y Mediana de $84\%$.
* **Morfología de la Forma:** Debido a que la media es menor que la mediana ($\text{Media} < \text{Mediana}$), la distribución exhibe un **sesgo negativo o asimetría hacia la izquierda**. Esto indica la presencia de una cola alargada en los valores bajos del histograma, provocada por un grupo de alumnos con notas bajas que arrastran el promedio general hacia atrás.
* **Dispersión:** El rango absoluto se sitúa cerca de los $38$ puntos, abarcando calificaciones desde un límite inferior de $60$ hasta una nota máxima sobresaliente de $98$.

### 3. Examen 3: Distribución Bimodal Simétrica
* **Métricas Centrales:** Media aritmética de $77\%$ y Mediana de $80\%$.
* **Morfología de la Forma:** La distribución presenta un comportamiento **bimodal**, caracterizado por exhibir dos picos de frecuencias independientes bien definidos en el histograma. Cada una de las modas locales posee colas uniformes en sus extremos, lo que demuestra que ambos componentes actúan de forma simétrica de manera aislada.
* **Dispersión:** El rango total del examen es el más amplio del estudio con $42$ puntos de dispersión, albergando una calificación mínima de $56$ y una máxima de $98$.

### 4. Examen Final: Distribución Simétrica Compacta
* **Métricas Centrales:** Media aritmética de $80\%$ y Mediana de $80\%$.
* **Morfología de la Forma:** Al coincidir nuevamente los dos estadísticos principales de tendencia central, la distribución se consolida como **simétrica**. La densidad de frecuencias decrece de forma balanceada y proporcional a medida que se aleja del centro hacia los límites laterales de las colas.
* **Dispersión y Anomalías:** Representa el examen con menor variabilidad del set con un rango estrecho de apenas $30$ puntos (límites de $68$ a $98$). Se identifica **un valor atípico (*outlier*)** ubicado de forma aislada en el extremo superior derecho, correspondiente al estudiante con rendimiento de excelencia que alcanzó el puntaje de $98$.

---

## Conceptos Estadísticos Aplicados

* **Relación entre Media y Mediana como Indicador de Sesgo**:
  * Si $\text{Media} == \text{Mediana}$, la distribución es **Simétrica**.
  * Si $\text{Media} < \text{Mediana}$, la distribución tiene **Asimetría Negativa o a la Izquierda** (*Left-Skewed*).
  * Si $\text{Media} > \text{Mediana}$, la distribución tiene **Asimetría Positiva o a la Derecha** (*Right-Skewed*).
* **Multimodalidad**: Fenómeno estadístico que ocurre cuando un dataset refleja más de un valor común o pico de frecuencia alta. En entornos educativos, una distribución bimodal suele indicar que la muestra está compuesta por dos subpoblaciones diferenciadas (por ejemplo, un grupo de alumnos que asimiló correctamente los conceptos y otro que requiere reforzamiento pedagógico).
* **Criterio de Valores Atípicos (*Outliers*)**: Registros que se distancian de forma extrema del patrón de comportamiento general de la población. Visualmente se localizan como barras aisladas separadas por espacios vacíos de datos (*gaps*) respecto al cuerpo denso del histograma.
