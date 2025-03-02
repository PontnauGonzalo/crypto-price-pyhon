from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route('/')
def inicio():
    # Clave API desde .env
    clave_api = os.getenv('CMC_API_KEY')
    
    # API de CoinMarketCap
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    # Parámetros para la solicitud API
    parametros = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }
    
    # Encabezados incluyendo tu clave API
    encabezados = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': clave_api,
    }
    
    # Solicitud API
    respuesta = requests.get(url, headers=encabezados, params=parametros)
    
    # 200=OK, 400=Bad Request, 401=Unauthorized, 500=Internal Server Error
    if respuesta.status_code == 200:
        datos = respuesta.json()
        # Extraer datos de criptomonedas
        criptomonedas = datos['data']
        return render_template('index.html', criptomonedas=criptomonedas)
    else:
        # Manejo de errores
        mensaje_error = f"Error: {respuesta.status_code}"
        return render_template('index.html', error=mensaje_error)

if __name__ == '__main__':
    app.run(debug=True)