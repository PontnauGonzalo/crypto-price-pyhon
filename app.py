"""Aplicación web para mostrar información de criptomonedas y noticias"""

from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)


@app.route("/")
def inicio():
    """Ruta para mostrar información de criptomonedas"""

    # Clave API desde .env
    clave_api = os.getenv("CMC_API_KEY")

    # API de CoinMarketCap
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # Parámetros para la solicitud API
    parametros = {"start": "1", "limit": "10", "convert": "USD"}

    # Encabezados incluyendo tu clave API
    encabezados = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": clave_api,
    }

    # Obtener fecha y hora actual para mostrar en la página
    momento_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Solicitud API
    respuesta = requests.get(url, headers=encabezados, params=parametros)

    # 200=OK, 400=Bad Request, 401=Unauthorized, 500=Internal Server Error
    if respuesta.status_code == 200:
        datos = respuesta.json()
        # Extraer datos de criptomonedas
        criptomonedas = datos["data"]
        return render_template(
            "index.html", criptomonedas=criptomonedas, momento_actual=momento_actual
        )
    else:
        # Manejo de errores
        mensaje_error = f"Error: {respuesta.status_code}"
        return render_template(
            "index.html", error=mensaje_error, momento_actual=momento_actual
        )


@app.route("/noticias")
def noticias():
    """Ruta para mostrar noticias de criptomonedas"""

    # Clave API desde .env
    clave_api = os.getenv("CMC_API_KEY")

    # API de CoinMarketCap para noticias
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/news"

    # Parámetros para la solicitud API de noticias
    parametros = {
        "limit": 10,  # Limitar a 10 noticias
        "sort": "relevance_desc",  # Ordenar por relevancia
        "language": "es,en",  # Preferencia por noticias en español, luego inglés
    }

    # Encabezados incluyendo tu clave API
    encabezados = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": clave_api,
    }

    momento_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        # Solicitud a la API de noticias
        respuesta = requests.get(url, headers=encabezados, params=parametros)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            noticias_api = datos.get("data", [])

            # Formatear las noticias para la plantilla
            noticias_formateadas = []
            for noticia in noticias_api:
                fecha_publicacion = datetime.fromtimestamp(
                    noticia.get("published_at", 0)
                ).strftime("%d/%m/%Y")
                noticias_formateadas.append(
                    {
                        "titulo": noticia.get("title", "Sin título"),
                        "descripcion": noticia.get(
                            "description", "Sin descripción disponible"
                        ),
                        "url": noticia.get("url", "#"),
                        "imagen": noticia.get("imageurl", None),
                        "fecha": fecha_publicacion,
                        "fuente": noticia.get("source", "CoinMarketCap"),
                    }
                )

            if not noticias_formateadas:
                mensaje_advertencia = "No se encontraron noticias para mostrar."
                return render_template(
                    "noticias.html",
                    noticias=[],
                    mensaje_advertencia=mensaje_advertencia,
                    momento_actual=momento_actual,
                )

            return render_template(
                "noticias.html",
                noticias=noticias_formateadas,
                momento_actual=momento_actual,
            )
        else:
            mensaje_error = f"Error al obtener noticias: Código {respuesta.status_code}"
            return render_template(
                "noticias.html", error=mensaje_error, momento_actual=momento_actual
            )

    except Exception as e:
        mensaje_error = f"Error al cargar noticias: {str(e)}"
        return render_template(
            "noticias.html", error=mensaje_error, momento_actual=momento_actual
        )


@app.route("/mercado")
def mercado():
    """Ruta para mostrar estadísticas globales del mercado de criptomonedas"""

    # Clave API desde .env
    clave_api = os.getenv("CMC_API_KEY")

    # API de CoinMarketCap para métricas globales
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

    # Encabezados incluyendo tu clave API
    encabezados = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": clave_api,
    }

    # Obtener fecha y hora actual para mostrar en la página
    momento_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        # Solicitud API para métricas globales
        respuesta = requests.get(url, headers=encabezados)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            metricas = datos["data"]

            return render_template(
                "mercado.html", metricas=metricas, momento_actual=momento_actual
            )
        else:
            mensaje_error = (
                f"Error al obtener datos del mercado: Código {respuesta.status_code}"
            )
            return render_template(
                "mercado.html", error=mensaje_error, momento_actual=momento_actual
            )

    except Exception as e:
        mensaje_error = f"Error al cargar datos del mercado: {str(e)}"
        return render_template(
            "mercado.html", error=mensaje_error, momento_actual=momento_actual
        )


if __name__ == "__main__":
    app.run(debug=True)
