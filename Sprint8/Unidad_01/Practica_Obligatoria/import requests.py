import requests

# Define la URL base de la API SIAR
base_url = "https://o.mapama.gob.es/apisiar/API/v1/"

# Define tu clave API
api_key = "SQrc18zRmSxZbZ5uK-VTu_-jUyrFpLbrRef4JDFLcZedXczxP"

# Define los parámetros de la consulta
# Aquí debes especificar la información que quieres obtener
# Consulta la documentación de la API SIAR para más detalles sobre los parámetros disponibles
params = {
    "clave": api_key,
    "fechaIni": "2020-01-01",  # Fecha de inicio
    "fechaFin": "2023-12-31",  # Fecha de fin
    "codigosEstacion": "5001",  # Código de la estación meteorológica (Campo de Cartagena)
    "tipoDatos": "diarios",  # Tipo de datos (diarios, horarios, etc.)
    # ... otros parámetros según tus necesidades
}

# Construye la URL completa de la petición
endpoint = "DatosAgroclimáticos"  # Endpoint para obtener datos agroclimáticos
url = f"{base_url}{endpoint}"

# Realiza la petición a la API
response = requests.get(url, params=params)

# Verifica si la petición fue exitosa
if response.status_code == 200:
    # Procesa los datos obtenidos
    data = response.json()
    # ... aquí puedes acceder a los datos y realizar tu análisis
    print(data)  # Imprime los datos en la consola
else:
    # Imprime un mensaje de error
    print(f"Error en la petición: {response.status_code}")
    print(response.text)  # Imprime la respuesta de la API para obtener más información sobre el error
    