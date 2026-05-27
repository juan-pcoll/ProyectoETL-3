# ETL Pipeline – Análisis de Condiciones de Vida y Pobreza

# Descripción del Proyecto
Dentro de este repositorio se encontrará todo el proyecto a desarrollar dentro de la clase de ETL con una **evaluación del Índice de Pobreza Multidimensional en Colombia – 2023** 
Autores: Juan Pablo Coll Muriel Miguel Ángel Echeverry Fernández Samuel Peña García

Objetivo del Proyecto Este proyecto tiene como finalidad realizar una evaluación estadística y estructurada del Índice de Pobreza Multidimensional (IPM) en Colombia para el año 2023, utilizando datos oficiales del DANE.

Más allá del cumplimiento académico, esta iniciativa busca: **Transformar datos crudos en información estructurada y analítica**. Visualizar indicadores clave que permitan comprender la realidad social del país. Aportar al análisis relacionado con los Objetivos de Desarrollo Sostenible (ODS), especialmente el ODS 1: Fin de la pobreza. Facilitar que terceros puedan reutilizar esta información como base para investigaciones, análisis de políticas públicas o generación de conciencia social basada en datos.

Este proyecto demuestra cómo la ingeniería de datos puede convertirse en una herramienta poderosa para la comprensión de problemáticas estructurales. Fuente de Datos

Los datos utilizados fueron obtenidos del **Departamento Administrativo Nacional de Estadística (DANE)**. 
Catálogo del estudio: https://microdatos.dane.gov.co/index.php/catalog/824/study-description Descarga de microdatos: https://microdatos.dane.gov.co/index.php/catalog/824/get-microdata Diccionario de variables: https://microdatos.dane.gov.co/index.php/catalog/824/data-dictionary/F45?file_name=Personas%20%20(departamental)

Características del Dataset Año: 2023 y 2024 Nivel: Personas (departamental) Formato original: .csv Datos públicos y de libre uso Variables codificadas (cada pregunta representada por un código) Respuestas numéricas asociadas a categorías específicas Preguntas mayoritariamente cerradas y de opción múltiple

Se utilizó la **API del World Bank para complementar el dataset con indicadores macroeconómicos**:

Variables integradas:
poverty_rate
unemployment_rate
gdp_per_capita
gini_index
Estas variables se integran mediante la columna:

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** para procesar datos relacionados con condiciones socioeconómicas de la población.

Los datos se limpian, transforman y almacenan en un **Data Warehouse en PostgreSQL** usando un **modelo estrella (Star Schema)** para facilitar el análisis.

El objetivo es permitir el análisis de indicadores como:

* Nivel educativo
* Acceso a salud
* Acceso a tecnología
* Condición laboral
* Distribución demográfica

# Diccionario de datos
Aquí se presenta el diccionario de datos, en el cual se puede consultar el significado de algunas secuencias numéricas presentes en la base de datos. Estas secuencias corresponden a códigos utilizados en el dataset que, por sí solos, no permiten identificar su significado. Por lo tanto, el diccionario de datos resulta fundamental para interpretar correctamente cada variable y comprender el valor que representan dichos códigos.

**secuencia_encuesta**

**secuencia_p**

**orden**

**P6051**(¿Cuál es el parentesco de ... con el jefe o la jefa de este hogar?)
1 Jefe (a) del hogar
2 Pareja, esposo(a), cónyuge, compañero(a)
3 Hijo(a), hijastro(a)
4 Nieto(a)
5 Padre, madre, padrastro, madrastra
6 Suegro o suegra
7 Hermano(a), hemanastro(a)
8 Yerno, nuera
9 Otro(a) pariente del(de la) jefe(a)
10 Empleado(a) del servicio doméstico
11 Parientes del servicio doméstico
12 Trabajador
13 Pensionista
14 Otro(a) no pariente

**P6020**(Sexo)
1 Hombre
2 Mujer

**P6040**(¿Cuántos años cumplidos tiene?)

**Factor de Expansión (FEX_C)**

**P6090**(¿Está afiliado, es cotizante o es beneficiario de alguna entidad de seguridad social en salud? (entidad promotora de salud -eps o administradora de régimen subsidiado -ars (a través del sisben)))
1 Sí
2 No
3 No sabe, no informa

**P5665**(En los últimos 30 días, ¿tuvo alguna enfermedad, accidente , problema odontológico o algún otro problema de salud que no haya implicado hospitalización)
1 Sí
2 No

**P8563**(Para tratar ese problema de salud, ¿qué hizo principalmente _____?)
1 Acudió a Institución prestadora de servicios de salud
2 Acudió a un médico general, especialista, odontólogo, terapeuta o profesional de la salud independiente ( de forma particular)
3 Acudió a un boticario, farmaceuta, droguista
4 Consultó a un tegua, empírico, curandero, yerbatero, comadrona
5 Asistió a terapias alternativas (acupuntura, esencias florales, musicoterapias, homeópata etc.)
6 Usó remedios caseros
7 Se autorecetó
8 Nada

**P51**(¿Dónde o con quién permanece… durante la mayor parte del tiempo entre semana?)
1 Asiste a un hogar comunitario, guardería , jardín o centro de desarrollo infantil.
2 Con su padre o madre en la casa
3 Con su padre o madre en el trabajo
4 Con empleada o niñera en la casa
5 Al cuidado de un pariente de 18 años o más
6 Al cuidado de un pariente menor de 18 años
7 En casa solo
8 Otro, ¿Cuál?

**P55**(¿Recibe o toma <...> desayuno o almuerzo en el lugar donde permanece la mayor parte del tiempo entre semana?)
1 Si
2 No

**P774**(¿paga por esta alimentación?)
1 Si, completamente
2 Si, por un pago simbólico
3 No paga, lo recibe en otro hogar o en la institución a la que asiste
4 No paga, lo recibe o lo lleva del hogar

**P6160**(¿sabe leer y escribir?)
1 Si
2 No

**P8586**(¿actualmente estudia? (asiste al preescolar, escuela, colegio o universidad))
1 Si
2 No

**P8587**(¿Cuál es el nivel educativo más alto alcanzado por ... y el último año o grado aprobado en este nivel?)
1 Ninguno
2 Preescolar
3 Básica Primaria (1º - 5º)
4 Básica secundaria (6º--9º)
5 Media (10º--13º)
6 Técnico sin título
7 Técnico con título
8 Tecnológico sin título
9 Tecnológico con título
10 Universitario sin titulo
11 Universitario con titulo
12 Postgrado sin titulo
13 Postgrado con titulo

**P8587S1**(Grado o año aprobado)

**P1088**(En qué nivel está matriculado y qué grado cursa?)
1 Preescolar (1 a 3)
2 Básica Primaria (1 a 5)
3 Básica secundaria (6 a 9)
4 Media (10 a 13)
5 Técnico
6 Tecnológico
7 Universitario
8 Postgrado

**P1088S1**(Grado o año que cursa)

**P6180**(¿recibe en el plantel educativo alimentos (desayunos, medias nueves, almuerzos, etc.) en forma gratuita o por un pago simbólico?)
1 Si
2 No

**P6240**(¿En que actividad ocupó...... la mayor parte del tiempo LA SEMANA PASADA?)
1 Trabajando
2 Buscando trabajo
3 Estudiando
4 Oficios del hogar
5 Incapacitado permanentemente para trabajar
6 Otra actividad ¿cuál?

**P6250**(Además de lo anterior, ¿.....realizó LA SEMANA PASADA alguna actividad paga por una hora o más?)
1 Si
2 No

**P6260**(Aunque no trabajó LA SEMANA PASADA, por una HORA O MÁS en forma remunerada, ¿tenía durante esa semana algún trabajo o negocio por el que recibe ingresos?)
1 Si
2 No

**P6270**(¿trabajó LA SEMANA PASADA en un negocio por UNA HORA O MÁS sin que le pagaran?)
1 Si
2 No

**P6351**(Si le hubiera resultado algún trabajo a …. ¿estaba disponible LA SEMANA PASADA para empezar a trabajar?)
1 Si
2 No

**P6390**(¿A qué actividad se dedica principalmente la empresa o negocio en la que ... realiza su trabajo?)

**P7250**(¿Durante cuántas semanas ha estado o estuvo <...> buscando trabajo?)

**P6920**(¿Está cotizando actualmente a un fondo de pensiones?)
1 Si
2 No
3 Ya es pesnionado

**P3336S1**(¿En qué modalidad(es) o a través de qué medio(s) se encuentra estudiando ... actualmente?)

**P3336S2**(¿En qué modalidad(es) o a través de qué medio(s) se encuentra estudiando ... actualmente? 2. Virtual (a través de internet en computador de escritorio, portátil, tableta o celular))

**P3336S3**(¿En qué modalidad(es) o a través de qué medio(s) se encuentra estudiando ... actualmente? 3. Alternancia entre presencial y virtual)

**P3337**(¿tuvo comunicación con sus maestros la semana pasada?)

**P1082S2**(¿Tiene Teléfono celular inteligente (smartphone)?)

---

# Arquitectura del Proyecto
Raw Data (CSV 2023 + 2024)
        ↓
Extract (Python)
        ↓
Clean (Validación estructural)
        ↓
Transform (Modelo estrella)
        ↓
Merge API Indicators
        ↓
Quality Check (Great Expectations)
        ↓
Load (PostgreSQL + CSV)
        ↓
Visualization (Power BI)

---

# Estructura del Proyecto

```
project_1/
│
├── airflow/
│   └── dags/
│       └── etl-dag.py
|
├── data/
│   ├── raw/
│   │   └── personas(departamental)2023-CEP.csv
│   │
│   └── processed/
│       ├── dim_demografia.csv
│       ├── dim_educacion.csv
│       ├── dim_tecnologia.csv
│       ├── dim_salud.csv
│       ├── dim_trabajo.csv
│       └── fact_persona.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│   └── validate.py
|   └── clean.py
|   └── dictionaries.py
|   └── extract_api.py
|   └── fusion.py
└── README.md
```

---

# Pipeline ETL

**Orquestación del Pipeline con Apache Airflow**

El pipeline ETL fue automatizado utilizando Apache Airflow, lo que permitió estructurar y ejecutar cada etapa del proceso de manera ordenada, reproducible y escalable.

Airflow se encarga de coordinar la ejecución de las tareas definidas dentro del flujo ETL mediante un DAG (Directed Acyclic Graph).

El flujo del pipeline implementado es:

Extract → Clean → Transform → Validate → Load

Cada etapa corresponde a una tarea independiente dentro del DAG.

## Extract

Carga los datos desde el archivo CSV.
```python
df = extract_data()
```
Los datos originales provienen de encuestas socioeconómicas:
personas(departamental) 2023
personas(departamental) 2024

---

# fusion

Durante esta etapa del pipeline ETL se realizó la integración de múltiples fuentes de datos con el objetivo de construir una estructura analítica unificada y consistente.

Esta fase permitió combinar información proveniente de:

dataset de personas 2023
dataset de personas 2024
indicadores macroeconómicos externos obtenidos mediante API
dimensiones generadas en el modelo estrella

La fusión de datos se realizó utilizando claves comunes como:

- year
- sexo
- edad
- nivel educativo
- condición laboral

permitiendo consolidar la información en una sola estructura analítica.

# Transform

Se realizan varios procesos de limpieza:

* Normalización de nombres de columnas
* Eliminación de inconsistencias
* Conversión de tipos de datos
* Creación de variables derivadas
Además se construye un **modelo dimensional**.

---

**Validación de Calidad de Datos con Great Expectations**

Para garantizar la integridad y confiabilidad de la información procesada, se implementó una etapa de validación automática de calidad de datos utilizando la librería Great Expectations.

Esta fase permite verificar que los datos cumplan reglas definidas antes de ser cargados en el Data Warehouse.

Las validaciones aplicadas incluyen:

Verificación de claves primarias únicas en la tabla fact_persona
Validación de valores no nulos en claves sustitutas (*_sk)
Control del número mínimo esperado de registros
Validación de consistencia entre dimensiones y tabla de hechos
Verificación de rangos válidos en variables numéricas

Ejemplo de validación aplicada:

validator.expect_column_values_to_not_be_null("persona_fact_id")
validator.expect_column_values_to_be_unique("persona_fact_id")

Estas reglas funcionan como un mecanismo de control similar a pruebas unitarias, pero aplicadas a los datos del pipeline ETL.

---

## ⭐ Modelo Estrella (Star Schema)

El Data Warehouse se organiza en:

### Fact Table
```
fact_persona
```
Contiene métricas y llaves a dimensiones.

---

### Dimensiones

```
dim_demografia
dim_educacion
dim_tecnologia
dim_salud
dim_trabajo
```
Cada dimensión describe un aspecto de la persona.

---

# Base de Datos

Se usa **PostgreSQL** como Data Warehouse y tambien se hace crea un warehouse dentro de la misma carpeta por si dado caso no es utilizada la aplicacion.

Configuración de conexión:

```
postgresql+psycopg2://postgres:password@localhost:5432/ods_pobreza
```

Las tablas se cargan automáticamente desde Python.

---

# Cómo ejecutar el proyecto

---

# Clonar el repositorio

```
git clone <repo>
cd project_1
```

---

# Instalar dependencias

```
pip install pandas sqlalchemy psycopg2-binary
```

---

# Crear base de datos en PostgreSQL

Este paso solo es si se va a utilizar postgreSQL si en dado caso no va hacer uso de este saltar este paso
```
CREATE DATABASE ods_pobreza;
```

---

# Ejecutar el pipeline

```
python src/main.py
```

Esto ejecutará:

```
Extract → Transform → Load
```

---
# ejecutar con airflow

Antes de ejecutar el pipeline, es necesario tener instalado:

- Docker
- Docker Compose

Verificar instalación:

docker --version
docker compose version
Iniciar Airflow con Docker

Desde la carpeta:

airflow/

ejecutar:

**docker compose up -d**

Esto inicia automáticamente los servicios:

Airflow Scheduler
Airflow Webserver
Airflow Worker
PostgreSQL
Redis

**Abrir en el navegador:**

**http://localhost:8085**

Credenciales por defecto:

usuario: airflow
contraseña: airflow

# Si se realizan cambios en el código del pipeline:

**docker compose restart**

Si se modifican dependencias o configuración:

**docker compose down**
**docker compose up -d**

-- 

# Ejemplos de consultas SQL

### Distribución por sexo

```sql
SELECT 
    d.sexo,
    COUNT(*) AS total_personas
FROM fact_persona f
JOIN dim_demografia d
ON f.demografia_sk = d.demografia_sk
GROUP BY d.sexo;
```

---

### Acceso a smartphone

```sql
SELECT 
    t.celular_inteligente,
    COUNT(*) AS total_personas
FROM fact_persona f
JOIN dim_tecnologia t
ON f.tecnologia_sk = t.tecnologia_sk
GROUP BY t.celular_inteligente;
```

---

### Nivel educativo

```sql
SELECT 
    e.nivel_educativo_alcanzado,
    COUNT(*) AS total_personas
FROM fact_persona f
JOIN dim_educacion e
ON f.educacion_sk = e.educacion_sk
GROUP BY e.nivel_educativo_alcanzado;
```

---

# Tecnologías utilizadas

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2
* Power BI (opcional)

---
#   P r o y e c t 2 - E T L - C E P 
 
 