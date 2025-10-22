#  Análisis de Desempeño en Cursos Introductorios de Matemática (2020–2025)

## 🎯 Introducción
Este proyecto analiza los resultados académicos de los estudiantes en la asignatura **Matemática Para Ingeniería** de la Facultad de Ingeniería de la Universidad Nacional de La Plata. Los datos son de producción propia, recopilados en los cursos en los que he participado **entre los años 2020 y 2025**.  

El objetivo principal es **caracterizar** el desempeño de los alumnos en general y a lo largo de los años, y **comparar el rendimiento de los alumnos en las distintas modalidades de cursada** (Verano, 1er Semestre y Anticipada). Se busca identificar tendencias a lo largo del tiempo y evaluar factores contextuales que expliquen las posibles diferencias entre las distintas modalidades. También se exploraron distintas posibilidades de modelos de Machine Learning para predecir los resultados de acuerdo a los datos presentes. 

El análisis se realiza en **Python** utilizando `pandas`, `matplotlib` y `seaborn`. Por confidencialidad, no se comparten los datos originales completos, pero se disponen los datos suficientes para replicar los resultados de este estudio.

---

## 📑 Estructura del Informe

Los resultados del análisis descriptivo de los cursos puede verse en el notebook [Analisis.ipynb](https://github.com/juanjogervasio/Intro-courses-analysis/blob/main/notebooks/Analisis.ipynb) y consta de las siguientes secciones:

### 1. Análisis exploratorio de los datos
- Descripción detallada del dataset (1221 registros, 13 variables).
- Variables principales: condición final, año, tipo de cursada, nota final.
- Identificación de categorías y estructura de los datos.

### 1.1 Distribución de datos por categorías
- Distribución de alumnos por **año y tipo de cursada**.
- Análisis de **cantidades de inscriptos** y dispersión según modalidad.
- Visualización de tendencias en la inscripción a lo largo de los años.
- Proporciones de alumnos **Promocionados, Desaprobados, Abandonados y Libres**.
- Evolución anual de estas categorías.
- Relación entre la variación de alumnos **Libres** y la tasa de **Promoción**.

### 1.2 Desempeño anual de cada curso
- Comparación detallada del desempeño por **año y tipo de cursada**.
- Representación en gráficos de proporciones.
- Discusión de casos particulares.

### 1.3 Distribución de datos por nota final
- Distribución de alumnos promocionados según nota final.
- Estadísticas descriptivas (media, moda, desviación estándar)
- Comparación entre promocionados de distintas modalidades.

### 2. Análisis de resultados según Tipo de Cursada
- Perfil general del **desempeño durante los cursos de 1er Semestre y Anticipada** en términos de:
  - Distribución de condición final y diferencias respecto al promedio grobal.
  - Curvas de supervivencia y evolución de la tasa de abandono para caracterizar permanencia de los alumnos durante la cursada.
  - Distribución de notas en los parciales.
- Comparación de resultados entre cada modalidad de cursada.   
---

## 📈 Modelos Predictivos de Desempeño

Se propuso un modelo de Logistic Regressor ajustado sobre los datos para predecir la Condición Final de los alumnos en base a sus resultados en los parciales. Fue necesaria una limpieza de los datos y realizar la elección de la porción de datos sobre los cuales entrenar y evaluar el modelo, para evitar sesgos del propio dataset. 

La construcción del modelo y los resultados obtenidos pueden verse en el notebook [Predictivos.ipynb](https://github.com/juanjogervasio/Intro-courses-analysis/blob/main/notebooks/Predictivos.ipynb)

---

## 🚀 Próximos pasos
- Profundizar las conclusiones obtenidas del análisis.
- Explorar más técnicas de **Machine Learning**, por ejemplo:
  - Analizar el desempeño del modelo de Logistic Regressor según se conocen los resultados de los sucesivos parciales.
  - Modelos predictivos más complejos.
  - Clusterización de perfiles de estudiantes.
