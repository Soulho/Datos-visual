# split_csv_pandas_func.py
import pandas as pd
import numpy as np  # <— usa NumPy en vez de pd.np

def split_csv_en_tres(input_csv: str, prefix: str = "parte",
                      shuffle: bool = True, seed: int | None = 42) -> tuple[str, str, str]:
    """
    Lee un CSV y lo divide en 3 archivos ~iguales.
    - input_csv: ruta del CSV de entrada
    - prefix: prefijo para los archivos de salida
    - shuffle: si True, baraja las filas antes de dividir
    - seed: semilla para reproducibilidad (usa None para aleatorio no determinista)
    """
    df = pd.read_csv(input_csv)

    if shuffle:
        df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    # Divide en 3 partes casi iguales
    partes = list(np.array_split(df, 3))

    rutas = [f"{prefix}_1.csv", f"{prefix}_2.csv", f"{prefix}_3.csv"]
    for parte, ruta in zip(partes, rutas):
        parte.to_csv(ruta, index=False)

    return tuple(rutas)

# Ejemplo de uso:
if __name__ == "__main__":
    p1, p2, p3 = split_csv_en_tres("TerriData_Dim4.csv", prefix="salida", shuffle=True, seed=123)
    print("Generados:", p1, p2, p3)