# ETL Pipeline – Índice de Pobreza Multidimensional en Colombia

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192)
![Apache Airflow](https://img.shields.io/badge/Airflow-Orchestration-red)
![Power BI](https://img.shields.io/badge/PowerBI-Visualization-yellow)
![Great Expectations](https://img.shields.io/badge/GreatExpectations-DataQuality-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Proyecto ETL orientado al análisis de condiciones de vida y pobreza multidimensional en Colombia utilizando datos oficiales del DANE y procesamiento analítico mediante un Data Warehouse en PostgreSQL.

---

# Tabla de Contenido

- Descripción del Proyecto
- Objetivos
- Fuente de Datos
- Arquitectura del Proyecto
- Pipeline ETL
- Modelo Estrella
- Diccionario de Datos
- Estructura del Proyecto
- Base de Datos
- Ejecución del Proyecto
- Ejecución con Airflow
- Consultas SQL
- Tecnologías Utilizadas
- Autores

---

# Descripción del Proyecto

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para procesar información relacionada con condiciones socioeconómicas de la población colombiana.

Los datos son limpiados, transformados y almacenados en un Data Warehouse utilizando un modelo estrella (Star Schema), permitiendo realizar análisis sobre:

- Nivel educativo
- Acceso a salud
- Acceso a tecnología
- Condición laboral
- Variables demográficas
- Indicadores de pobreza

---

# Objetivos del Proyecto

Este proyecto busca:

- Transformar datos crudos en información estructurada y analítica
- Facilitar el análisis del Índice de Pobreza Multidimensional (IPM)
- Integrar indicadores macroeconómicos externos
- Aplicar procesos de calidad de datos
- Implementar arquitectura ETL automatizada
- Facilitar visualización y análisis en Power BI

---

# Fuente de Datos

Los datos utilizados provienen del Departamento Administrativo Nacional de Estadística (DANE).

| Recurso | Enlace |
|---|---|
| Catálogo del estudio | https://microdatos.dane.gov.co/index.php/catalog/824/study-description |
| Descarga de microdatos | https://microdatos.dane.gov.co/index.php/catalog/824/get-microdata |
| Diccionario de variables | https://microdatos.dane.gov.co/index.php/catalog/824/data-dictionary/F45?file_name=Personas%20%20(departamental) |

---

# Características del Dataset

| Característica | Valor |
|---|---|
| Año | 2023 - 2024 |
| Nivel | Personas (departamental) |
| Formato | CSV |
| Tipo de datos | Públicos |
| Variables | Codificadas |
| Tipo de preguntas | Cerradas y opción múltiple |

---

# Integración de API Externa

Se utilizó la API del World Bank para complementar el dataset con indicadores macroeconómicos.

## Variables Integradas

| Variable | Descripción |
|---|---|
| poverty_rate | Tasa de pobreza |
| unemployment_rate | Tasa de desempleo |
| gdp_per_capita | PIB per cápita |
| gini_index | Índice de Gini |

---

# Arquitectura del Proyecto

```text
Raw CSV Data
      ↓
Extract
      ↓
Clean
      ↓
Transform
      ↓
Merge API Indicators
      ↓
Quality Validation
      ↓
Load PostgreSQL
      ↓
Power BI Visualization
```

---

# Pipeline ETL

El pipeline ETL fue automatizado utilizando Apache Airflow, permitiendo ejecutar cada etapa de forma ordenada y reproducible.

## Flujo del Pipeline

```text
Extract → Clean → Transform → Validate → Load
```

---

# Etapas del Pipeline

## Extract

Carga de datos desde archivos CSV.

```python
df = extract_data()
```

Datasets utilizados:

- personas(departamental)2023
- personas(departamental)2024

---

## Clean

Procesos de limpieza aplicados:

- Normalización de columnas
- Eliminación de inconsistencias
- Conversión de tipos de datos
- Tratamiento de valores faltantes

---

## Transform

Transformación de datos y construcción del modelo dimensional.

Procesos aplicados:

- Creación de dimensiones
- Construcción de tabla de hechos
- Variables derivadas
- Integración de indicadores externos

---

## Fusion

Integración de múltiples fuentes de información:

- Dataset 2023
- Dataset 2024
- API World Bank
- Dimensiones analíticas

Claves utilizadas:

- year
- sexo
- edad
- nivel educativo
- condición laboral

---

## Validate

Se implementó validación automática de calidad utilizando Great Expectations.

### Validaciones Aplicadas

| Validación | Descripción |
|---|---|
| Claves únicas | Validación de IDs únicos |
| Valores nulos | Control de campos obligatorios |
| Rangos válidos | Verificación de variables numéricas |
| Integridad dimensional | Consistencia entre dimensiones y hechos |

### Ejemplo

```python
validator.expect_column_values_to_not_be_null("persona_fact_id")
validator.expect_column_values_to_be_unique("persona_fact_id")
```

---

# Modelo Estrella (Star Schema)

## Fact Table

```text
fact_persona
```

Contiene métricas y claves relacionadas con las dimensiones.

---

## Dimensiones

```text
dim_demografia
dim_educacion
dim_tecnologia
dim_salud
dim_trabajo
```

Cada dimensión representa un aspecto específico de la persona.

---

# Diccionario de Datos

## Demografía

| Variable | Descripción | Valores |
|---|---|---|
| P6020 | Sexo | 1 = Hombre, 2 = Mujer |
| P6040 | Edad | Valor numérico |
| P6051 | Parentesco con jefe del hogar | 1-14 categorías |
| FEX_C | Factor de expansión | Valor numérico |

---

## Salud

| Variable | Descripción | Valores |
|---|---|---|
| P6090 | Afiliación a salud | 1 = Sí, 2 = No |
| P5665 | Enfermedad últimos 30 días | 1 = Sí, 2 = No |
| P8563 | Acción frente problema de salud | 1-8 categorías |

---

## Educación

| Variable | Descripción | Valores |
|---|---|---|
| P6160 | Sabe leer y escribir | 1 = Sí, 2 = No |
| P8586 | Actualmente estudia | 1 = Sí, 2 = No |
| P8587 | Nivel educativo alcanzado | 1-13 categorías |
| P1088 | Nivel matriculado | 1-8 categorías |
| P6180 | Alimentación escolar | 1 = Sí, 2 = No |

---

## Trabajo

| Variable | Descripción | Valores |
|---|---|---|
| P6240 | Actividad principal | 1-6 categorías |
| P6250 | Actividad paga | 1 = Sí, 2 = No |
| P6260 | Trabajo o negocio | 1 = Sí, 2 = No |
| P6270 | Trabajo sin pago | 1 = Sí, 2 = No |
| P6351 | Disponibilidad laboral | 1 = Sí, 2 = No |
| P7250 | Semanas buscando trabajo | Valor numérico |
| P6920 | Cotización pensión | 1 = Sí, 2 = No |

---

## Tecnología

| Variable | Descripción | Valores |
|---|---|---|
| P1082S2 | Smartphone | 1 = Sí, 2 = No |
| P3337 | Comunicación con maestros | 1 = Sí, 2 = No |

---

# Estructura del Proyecto

```text
project_1/
│
├── airflow/
│   └── dags/
│       └── etl-dag.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── clean.py
│   ├── transform.py
│   ├── fusion.py
│   ├── validate.py
│   ├── load.py
│   ├── extract_api.py
│   ├── dictionaries.py
│   └── main.py
│
└── README.md
```

---

# Base de Datos

Se utiliza PostgreSQL como Data Warehouse principal.

## Configuración

```python
postgresql+psycopg2://postgres:password@localhost:5432/ods_pobreza
```

Las tablas son cargadas automáticamente desde Python.

---

# Cómo Ejecutar el Proyecto

## Clonar Repositorio

```bash
git clone <repo>
cd project_1
```

---

## Instalar Dependencias

```bash
pip install pandas sqlalchemy psycopg2-binary
```

---

## Crear Base de Datos

```sql
CREATE DATABASE ods_pobreza;
```

---

## Ejecutar Pipeline

```bash
python src/main.py
```

---

# Ejecución con Apache Airflow

## Requisitos

- Docker
- Docker Compose

Verificar instalación:

```bash
docker --version
docker compose version
```

---

## Iniciar Airflow

Desde la carpeta:

```bash
airflow/
```

Ejecutar:

```bash
docker compose up -d
```

---

## Servicios Iniciados

- Airflow Scheduler
- Airflow Webserver
- Airflow Worker
- PostgreSQL
- Redis

---

## Acceso Web

```text
http://localhost:8085
```

### Credenciales

| Usuario | Contraseña |
|---|---|
| airflow | airflow |

---

## Reiniciar Servicios

```bash
docker compose restart
```

---

## Reiniciar Contenedores

```bash
docker compose down
docker compose up -d
```

---

# Ejemplos de Consultas SQL

## Distribución por Sexo

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

## Acceso a Smartphone

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

## Nivel Educativo

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

# Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| Python | Desarrollo ETL |
| Pandas | Transformación de datos |
| PostgreSQL | Data Warehouse |
| SQLAlchemy | Conexión ORM |
| psycopg2 | Conector PostgreSQL |
| Apache Airflow | Orquestación |
| Great Expectations | Calidad de datos |
| Power BI | Visualización |
| Docker | Contenedores |

---

# Autores

| Nombre |
|---|
| Juan Pablo Coll Muriel |
| Miguel Ángel Echeverry Fernández |
| Samuel Peña García |

---

# Conclusión

Este proyecto demuestra cómo la ingeniería de datos y los procesos ETL pueden utilizarse para transformar datos públicos en información analítica de valor, facilitando el análisis de pobreza multidimensional y condiciones de vida en Colombia.
