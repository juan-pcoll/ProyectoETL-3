import pandas as pd


def validate_data(tables):

    print("\n=== DATA VALIDATION ===")

    for name, df in tables.items():

        print(f"\nValidating table: {name}")

        # Validar dataframe vacío
        if df.empty:
            raise ValueError(f"{name} está vacía")

        # Validar nulls
        null_columns = df.columns[df.isnull().any()].tolist()

        if null_columns:
            raise ValueError(
                f"{name} tiene valores nulos en columnas: {null_columns}"
            )

        print(f"[OK] {name} validada correctamente")

    print("\n=== VALIDATION FINISHED ===")
