def validate_data(tables):

    print("\n=== VALIDATION ===")

    for name, df in tables.items():

        if df.empty:
            raise ValueError(f"La tabla {name} está vacía")

        nulls = df.isnull().sum().sum()

        if nulls > 0:
            print(f"[WARN] {name} contiene {nulls} valores nulos")

    print("=== VALIDATION FINISHED ===\n")

    return tables