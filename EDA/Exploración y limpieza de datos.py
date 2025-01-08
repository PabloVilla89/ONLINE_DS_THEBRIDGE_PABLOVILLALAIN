import pandas as pd
import glob
import matplotlib.pyplot as plt

lista_df = []

# Ruta relativa a la carpeta "datos"
archivos_csv = glob.glob('datos/informe_horario_para_usuarios (*).csv')

if not archivos_csv:
    print("¡No se encontraron archivos CSV en la carpeta 'datos'! Revisa que la carpeta exista y contenga los archivos.")
    exit()

for archivo in archivos_csv:
    try:
        df_temp = pd.read_csv(archivo, sep=';', decimal=',')
        lista_df.append(df_temp)
        print(f"Archivo leído correctamente: {archivo}")
    except pd.errors.ParserError as e:
        print(f"Error al analizar el archivo: {archivo}. Revisa los delimitadores, decimales y la estructura del archivo.\nError específico: {e}")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {archivo}")
    except Exception as e:
        print(f"Otro error al procesar el archivo {archivo}: {e}")

if not lista_df:
    print("Ningún DataFrame se leyó correctamente. Revisa los errores anteriores.")
    exit()

df = pd.concat(lista_df, ignore_index=True)

# Conversión de tipos y creación de columnas
columnas_numericas = ['DPV', 'DVMED', 'HRMAX', 'HRMED', 'HRMIN', 'PREC', 'DEWPT', 'RADMED', 'RRMED', 'RVIENTO', 'TMAX', 'TMED', 'TMIN', 'VVMAX', 'VVMED']
for columna in columnas_numericas:
    df[columna] = pd.to_numeric(df[columna], errors='coerce')

df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%y')
df['AÑO'] = df['FECHA'].dt.year

# Ejemplo de visualización
temperatura_media_anual = df.groupby('AÑO')['TMED'].mean()

plt.figure(figsize=(10, 6))
plt.plot(temperatura_media_anual.index, temperatura_media_anual.values, marker='o')
plt.xlabel('Año')
plt.ylabel('Temperatura Media Anual (°C)')
plt.title('Tendencia de la Temperatura Media Anual en Cartagena (2005-2024)')
plt.grid(True)
plt.show()

df.to_csv('datos_combinados_limpios.csv', index=False)
print("Datos guardados en datos_combinados_limpios.csv")