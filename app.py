"""Aplicación web para mostrar información de criptomonedas y noticias"""

from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from functools import lru_cache  # Decorador para caché de resultados
import time  # Módulo para medir tiempo de ejecución

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)


@app.route("/")
def inicio():
    """
    Ruta principal que muestra información de criptomonedas.

    Obtiene datos de las 10 principales criptomonedas desde CoinMarketCap
    y los renderiza en la plantilla index.html.

    Returns:
        flask.Response: Plantilla renderizada con datos o mensaje de error
    """

    clave_api = os.getenv("CMC_API_KEY")

    # API de CoinMarketCap
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # Parámetros para la solicitud API
    parametros = {"start": "1", "limit": "10", "convert": "USD"}

    # Encabezados incluyendo clave API
    encabezados = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": clave_api,
    }

    # Fecha y hora actual
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

    momento_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mensaje_advertencia = "La API de CoinMarketCap no proporciona acceso a noticias en su plan básico. Mostrando noticias de ejemplo."

    # Creamos noticias de ejemplo en lugar de hacer la llamada a la API
    noticias_ejemplo = [
        {
            "titulo": "Bitcoin supera los $60,000 por primera vez en más de un año",
            "descripcion": "La principal criptomoneda del mundo ha superado la barrera psicológica de los $60,000, impulsada por la reciente aprobación de ETFs de Bitcoin al contado y el aumento de la demanda institucional.",
            "url": "https://www.coindesk.com",
            "imagen": "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - CoinDesk",
        },
        {
            "titulo": "Ethereum completa actualización importante para mejorar escalabilidad",
            "descripcion": "La red Ethereum ha completado con éxito su última actualización, que promete reducir las tarifas de gas y aumentar significativamente la capacidad de procesamiento de transacciones en la red.",
            "url": "https://ethereum.org",
            "imagen": "https://acortar.link/MVkbnq",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - Ethereum.org",
        },
        {
            "titulo": "Reguladores europeos presentan nuevo marco para criptomonedas",
            "descripcion": "La Unión Europea ha anunciado un conjunto integral de reglas para regular el mercado de criptomonedas, buscando proteger a los inversores mientras se fomenta la innovación en el espacio blockchain.",
            "url": "https://europa.eu",
            "imagen": "https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - EU Commission",
        },
        {
            "titulo": "Nuevo récord: NFTs superan los $10 mil millones en ventas",
            "descripcion": "El mercado de tokens no fungibles (NFTs) continúa su crecimiento explosivo, superando los $10 mil millones en ventas totales, con el arte digital y los coleccionables liderando la tendencia.",
            "url": "https://opensea.io",
            "imagen": "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - OpenSea",
        },
        {
            "titulo": "El Salvador expande su infraestructura Bitcoin",
            "descripcion": "El gobierno de El Salvador ha anunciado planes para construir una 'Ciudad Bitcoin' alimentada por energía geotérmica, tras su histórica adopción de Bitcoin como moneda de curso legal.",
            "url": "https://www.bitcoinmagazine.com",
            "imagen": "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - Bitcoin Magazine",
        },
        {
            "titulo": "DeFi alcanza nuevo hito: $200 mil millones en valor total bloqueado",
            "descripcion": "El espacio de Finanzas Descentralizadas (DeFi) continúa creciendo a un ritmo acelerado, alcanzando los $200 mil millones en valor total bloqueado en diversos protocolos.",
            "url": "https://defipulse.com",
            "imagen": "https://images.unsplash.com/photo-1639762681057-408e52192e55?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - DeFi Pulse",
        },
    ]

    # Obtener noticias en caché
    noticias_ejemplo, _ = get_noticias_ejemplo()
        
    return render_template(
        "noticias.html",
        noticias=noticias_ejemplo,
        mensaje_advertencia=mensaje_advertencia,
        momento_actual=momento_actual,
    )


# Caché para las noticias (válido por 1 hora)
@lru_cache(maxsize=1)
def get_noticias_ejemplo():
    """Genera noticias de ejemplo y las guarda en caché por 1 hora"""
    # Genera timestamp diario para invalidar la caché después de 1 día
    cache_day = time.strftime("%Y-%m-%d")
    
    # Obtenemos la fecha actual para las noticias
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return [
        {
            "titulo": "Bitcoin supera los $60,000 por primera vez en más de un año",
            "descripcion": "La principal criptomoneda del mundo ha superado la barrera psicológica de los $60,000, impulsada por la reciente aprobación de ETFs de Bitcoin al contado y el aumento de la demanda institucional.",
            "url": "https://www.coindesk.com",
            "imagen": "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - CoinDesk",
        },
        {
            "titulo": "Ethereum completa actualización importante para mejorar escalabilidad",
            "descripcion": "La red Ethereum ha completado con éxito su última actualización, que promete reducir las tarifas de gas y aumentar significativamente la capacidad de procesamiento de transacciones en la red.",
            "url": "https://ethereum.org",
            "imagen": "https://acortar.link/MVkbnq",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - Ethereum.org",
        },
        {
            "titulo": "Reguladores europeos presentan nuevo marco para criptomonedas",
            "descripcion": "La Unión Europea ha anunciado un conjunto integral de reglas para regular el mercado de criptomonedas, buscando proteger a los inversores mientras se fomenta la innovación en el espacio blockchain.",
            "url": "https://europa.eu",
            "imagen": "https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - EU Commission",
        },
        {
            "titulo": "Nuevo récord: NFTs superan los $10 mil millones en ventas",
            "descripcion": "El mercado de tokens no fungibles (NFTs) continúa su crecimiento explosivo, superando los $10 mil millones en ventas totales, con el arte digital y los coleccionables liderando la tendencia.",
            "url": "https://opensea.io",
            "imagen": "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - OpenSea",
        },
        {
            "titulo": "El Salvador expande su infraestructura Bitcoin",
            "descripcion": "El gobierno de El Salvador ha anunciado planes para construir una 'Ciudad Bitcoin' alimentada por energía geotérmica, tras su histórica adopción de Bitcoin como moneda de curso legal.",
            "url": "https://www.bitcoinmagazine.com",
            "imagen": "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - Bitcoin Magazine",
        },
        {
            "titulo": "DeFi alcanza nuevo hito: $200 mil millones en valor total bloqueado",
            "descripcion": "El espacio de Finanzas Descentralizadas (DeFi) continúa creciendo a un ritmo acelerado, alcanzando los $200 mil millones en valor total bloqueado en diversos protocolos.",
            "url": "https://defipulse.com",
            "imagen": "https://images.unsplash.com/photo-1639762681057-408e52192e55?ixlib=rb-4.0.3",
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "fuente": "Ejemplo - DeFi Pulse",
        },
    ], cache_day


@app.route("/mercado")
def mercado():
    """Ruta para mostrar estadísticas globales del mercado de criptomonedas"""

    clave_api = os.getenv("CMC_API_KEY")

    # API de CoinMarketCap para métricas globales
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

    # Encabezados incluyendo la clave API
    encabezados = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": clave_api,
    }

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


# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
