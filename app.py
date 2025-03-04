""" Aplicación web para mostrar información de criptomonedas y noticias """

from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)


@app.route('/')
def inicio():
    """ Ruta para mostrar información de criptomonedas """

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

    # Obtener fecha y hora actual para mostrar en la página
    momento_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Solicitud API
    respuesta = requests.get(url, headers=encabezados, params=parametros)

    # 200=OK, 400=Bad Request, 401=Unauthorized, 500=Internal Server Error
    if respuesta.status_code == 200:
        datos = respuesta.json()
        # Extraer datos de criptomonedas
        criptomonedas = datos['data']
        return render_template('index.html', criptomonedas=criptomonedas, momento_actual=momento_actual)
    else:
        # Manejo de errores
        mensaje_error = f"Error: {respuesta.status_code}"
        return render_template('index.html', error=mensaje_error, momento_actual=momento_actual)


@app.route('/noticias')
def noticias():
    """ Ruta para mostrar noticias de criptomonedas """

    # Clave API desde .env
    # clave_api = os.getenv('CMC_API_KEY')

    # Puedes usar otra API para noticias o simular datos por ahora
    # Aquí simulamos algunos datos de noticias como ejemplo

    momento_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    try:
        # Esto sería reemplazado por una llamada a una API real de noticias
        noticias_ejemplo = [
            {
                "titulo": "Bitcoin alcanza nuevo máximo histórico",
                "fecha": "2 de marzo, 2025",
                "descripcion": "Bitcoin ha superado su máximo histórico tras el anuncio de importantes inversiones institucionales.",
                "url": "#"
            },
            {
                "titulo": "Ethereum completa actualización importante",
                "fecha": "1 de marzo, 2025",
                "descripcion": "La red Ethereum ha completado con éxito una actualización que mejora la escalabilidad y reduce las tarifas de gas.",
                "url": "#"
            },
            {
                "titulo": "Reguladores anuncian nuevas directrices para criptomonedas",
                "fecha": "28 de febrero, 2025",
                "descripcion": "Varios países han acordado un marco regulatorio común para activos digitales, proporcionando mayor claridad al mercado.",
                "url": "#"
            }
        ]

        return render_template('noticias.html', noticias=noticias_ejemplo, momento_actual=momento_actual)
    except Exception as e:
        mensaje_error = f"Error al cargar noticias: {str(e)}"
        return render_template('noticias.html', error=mensaje_error, momento_actual=momento_actual)


if __name__ == '__main__':
    app.run(debug=True)