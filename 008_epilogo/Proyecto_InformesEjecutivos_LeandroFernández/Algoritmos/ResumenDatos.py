import pandas as pd
import numpy as np
import re

def columna_numerica(columna, nombre_columna):
    nombre_columna_lower = nombre_columna.lower()
    if re.search(r'id|identificador|user', nombre_columna_lower):
        return False

    if columna.dtype == 'object':
        columna_limpia = columna.str.replace(r'[^\d.]', '', regex=True)
        num_convertidos = pd.to_numeric(columna_limpia, errors='coerce')
        if num_convertidos.notnull().mean() > 0.7:
            return True
    return columna.dtype in ['int64', 'float64']

def analizar_y_limpiar(data):
    df = data
    columnas_numericas = [col for col in df.columns if columna_numerica(df[col], col)]
    
    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    
    filas, columnas = df.shape
    print(f"El dataset tiene {filas} filas y {columnas} columnas.")
    
    valores_nulos = df.isnull().mean() * 100
    columnas_con_nulos = valores_nulos[valores_nulos > 0]
    
    if len(columnas_con_nulos) > 0:
        print(f"Las siguientes columnas tienen valores nulos: {', '.join(columnas_con_nulos.index)}. "
              f"El porcentaje de valores nulos es: {columnas_con_nulos.round(2).to_dict()}.")
        
        df.fillna(df.median(numeric_only=True), inplace=True)
        df.fillna("Desconocido", inplace=True)
        print("Se han imputado valores numéricos con la mediana y valores categóricos con 'Desconocido'.")
    
    total_outliers = 0
    for columna in columnas_numericas:
        q1 = df[columna].quantile(0.25)
        q3 = df[columna].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
        total_outliers += len(outliers)
        
        if not outliers.empty:
            df[columna] = np.where((df[columna] < limite_inferior) | (df[columna] > limite_superior),
                                   df[columna].median(), df[columna])
    
    if total_outliers > 0:
        print(f"Se encontraron un total de {total_outliers} outliers en las columnas numéricas, "
              "los cuales fueron reemplazados por la mediana.")
    
    if len(columnas_numericas) > 1:
        correlaciones = df[columnas_numericas].corr().round(2)
        print("\nCorrelaciones entre columnas numéricas:")
        print(correlaciones)
    
    resumen_final = df.describe().round(2)
    print("\nDescripción final del dataset después de la limpieza:")
    print(resumen_final)

    return df


# Ejemplo de uso
data = pd.read_csv('amazon.csv')  # Reemplaza con la ruta de tu archivo CSV
analizar_y_limpiar(data)
