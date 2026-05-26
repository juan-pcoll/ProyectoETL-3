import os
import pandas as pd


def clean_strings(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].apply(
                lambda x: str(x).encode("utf-8", "ignore").decode("utf-8") if isinstance(x, str) else x
            )
    return df


def load_data(tables, use_postgres=True):

    print("\n=== LOADING DATA ===")

    # -------------------------
    # Guardar siempre en CSV
    # -------------------------
    output_path = "data/processed"

    os.makedirs(output_path, exist_ok=True)

    for name, df in tables.items():

        file_path = os.path.join(output_path, f"{name}.csv")

        df.to_csv(file_path, index=False)

        print(f"  Saved CSV: {file_path} ({len(df)} filas, {len(df.columns)} columnas)")

    # -------------------------
    # Intentar cargar a PostgreSQL
    # -------------------------
    if use_postgres:

        try:

            from sqlalchemy import create_engine

            engine = create_engine(
                "postgresql+psycopg2://airflow:airflow@postgres:5432/ods_pobreza"
            )

            load_order = [
                "dim_demografia",
                "dim_educacion",
                "dim_tecnologia",
                "dim_tiempo",
                "dim_salud",
                "dim_trabajo",
                "fact_persona"
            ]

            for name in load_order:

                if name not in tables:
                    print(f"  [WARN] Tabla '{name}' no encontrada en tables, se omite")
                    continue

                df = tables[name]

                print(f"\nLoading table: {name}")
                print(df.dtypes)
                print(df.head())

                df = clean_strings(df)
                
                df.to_sql(
                    name,
                    engine,
                    if_exists="append",
                    index=False,
                    chunksize=10000  
                )

                print(f"  Loaded to PostgreSQL: {name} ({len(df)} filas)")

            print("\n  PostgreSQL load completado")

        except Exception as e:

            print(f"\n[ERROR] PostgreSQL load failed: {e}")
            raise

    print("\n=== LOAD FINISHED ===")