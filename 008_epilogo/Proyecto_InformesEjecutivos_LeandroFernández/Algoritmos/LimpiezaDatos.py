import pandas as pd
import numpy as np
import re

def columna_numerica(columna):
    """
    Heurística para detectar si una columna debe ser tratada como numérica.
    - Intenta convertir los valores a números, eliminando caracteres no numéricos.
    - Cuenta cuántos valores numéricos válidos puede extraer para decidir si es numérica.
    """
    if columna.dtype == 'object':
        # Remover caracteres comunes que impiden la conversión (símbolos de moneda, comas, etc.)
        columna_limpia = columna.str.replace(r'[^\d.]', '', regex=True)
        # Intentar convertir a numérico
        num_convertidos = pd.to_numeric(columna_limpia, errors='coerce')
        # Si más del 70% de los valores se pueden convertir a números, asumimos que es numérica
        if num_convertidos.notnull().mean() > 0.7:
            return True
    return columna.dtype in ['int64', 'float64']

def analizar_y_limpiar(data):
    # Cargar el archivo CSV
    df = data
    
    # Determinar qué columnas son numéricas
    columnas_numericas = [col for col in df.columns if columna_numerica(df[col])]
    
    # Convertir las columnas numéricas identificadas a formato numérico
    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    
    # Información general
    filas, columnas = df.shape
    print(f"El dataset tiene {filas} filas y {columnas} columnas.")
    
    # Identificar columnas con valores nulos y porcentaje de nulos
    valores_nulos = df.isnull().mean() * 100
    columnas_con_nulos = valores_nulos[valores_nulos > 0]
    
    # Si hay valores nulos
    if len(columnas_con_nulos) > 0:
        print("\nColumnas con valores nulos y su porcentaje:")
        print(columnas_con_nulos)
        
        # Proceso de limpieza (imputación o eliminación de filas)
        df.fillna(df.median(numeric_only=True), inplace=True)  # Imputar valores numéricos con la mediana
        df.fillna("Desconocido", inplace=True)  # Para valores categóricos, reemplazar con "Desconocido"
        print("\nLos valores nulos han sido reemplazados.")
    
    # Detección de outliers en columnas numéricas
    for columna in columnas_numericas:
        q1 = df[columna].quantile(0.25)
        q3 = df[columna].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
        if not outliers.empty:
            print(f"\nSe encontraron {len(outliers)} outliers en la columna '{columna}'.")
            # Reemplazar outliers con la mediana
            df[columna] = np.where((df[columna] < limite_inferior) | (df[columna] > limite_superior),
                                   df[columna].median(), df[columna])
            print(f"Los outliers en '{columna}' han sido reemplazados por la mediana.")
    
    # Correlaciones entre columnas numéricas
    if len(columnas_numericas) > 1:
        correlaciones = df[columnas_numericas].corr()
        print("\nCorrelaciones entre columnas numéricas:")
        print(correlaciones)
    
    # Resumen descriptivo después de la limpieza
    print("\nDescripción final del dataset después de la limpieza:")
    print(df.describe())

    describe = df.describe()

    return df
def columna_numerica(columna, nombre_columna):
    """
    Heurística para detectar si una columna debe ser tratada como numérica.
    - Excluye columnas como 'ID', 'User ID', 'Identificador', etc.
    - Intenta convertir los valores a números, eliminando caracteres no numéricos.
    - Cuenta cuántos valores numéricos válidos puede extraer para decidir si es numérica.
    """
    # Verificar si el nombre de la columna sugiere que es un identificador
    nombre_columna_lower = nombre_columna.lower()
    if re.search(r'id|identificador|user', nombre_columna_lower):
        return False

    # Proceder con el chequeo estándar para columnas numéricas
    if columna.dtype == 'object':
        # Remover caracteres comunes que impiden la conversión (símbolos de moneda, comas, etc.)
        columna_limpia = columna.str.replace(r'[^\d.]', '', regex=True)
        # Intentar convertir a numérico
        num_convertidos = pd.to_numeric(columna_limpia, errors='coerce')
        # Si más del 70% de los valores se pueden convertir a números, asumimos que es numérica
        if num_convertidos.notnull().mean() > 0.7:
            return True
    return columna.dtype in ['int64', 'float64']

def analizar_y_limpiar(data):
    # Cargar el archivo CSV
    df = data
    
    # Determinar qué columnas son numéricas
    columnas_numericas = [col for col in df.columns if columna_numerica(df[col], col)]
    
    # Convertir las columnas numéricas identificadas a formato numérico
    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    
    # Información general
    filas, columnas = df.shape
    print(f"El dataset tiene {filas} filas y {columnas} columnas.")
    
    # Identificar columnas con valores nulos y porcentaje de nulos
    valores_nulos = df.isnull().mean() * 100
    columnas_con_nulos = valores_nulos[valores_nulos > 0]
    
    # Si hay valores nulos
    if len(columnas_con_nulos) > 0:
        print("\nColumnas con valores nulos y su porcentaje:")
        print(columnas_con_nulos)
        
        # Proceso de limpieza (imputación o eliminación de filas)
        df.fillna(df.median(numeric_only=True), inplace=True)  # Imputar valores numéricos con la mediana
        df.fillna("Desconocido", inplace=True)  # Para valores categóricos, reemplazar con "Desconocido"
        print("\nLos valores nulos han sido reemplazados.")
    
    # Detección de outliers en columnas numéricas
    for columna in columnas_numericas:
        q1 = df[columna].quantile(0.25)
        q3 = df[columna].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
        if not outliers.empty:
            print(f"\nSe encontraron {len(outliers)} outliers en la columna '{columna}'.")
            # Reemplazar outliers con la mediana
            df[columna] = np.where((df[columna] < limite_inferior) | (df[columna] > limite_superior),
                                   df[columna].median(), df[columna])
            print(f"Los outliers en '{columna}' han sido reemplazados por la mediana.")
    
    # Correlaciones entre columnas numéricas
    if len(columnas_numericas) > 1:
        correlaciones = df[columnas_numericas].corr()
        print("\nCorrelaciones entre columnas numéricas:")
        print(correlaciones)
    
    # Resumen descriptivo después de la limpieza
    print("\nDescripción final del dataset después de la limpieza:")
    print(df.describe())

    describe = df.describe()

    return df