# Proyecto: Visualizador de Precios de Criptomonedas con CoinMarketCap API
[![Python](https://img.shields.io/badge/docs-Python-blue?logo=python)](https://docs.python.org/3/)
[![Flask](https://img.shields.io/badge/docs-Flask-green?logo=flask)](https://flask.palletsprojects.com/)
[![CoinMarketCap API](https://img.shields.io/badge/docs-CMC_API-white?logo=coinmarketcap)](https://coinmarketcap.com/api/documentation/v1/)
[![Demo en vivo](https://img.shields.io/badge/web-online-grey?logo=vercel)](https://crypto-price-visualizer-one.vercel.app/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/2a0a3551-c67c-49bb-b032-2249161c3999" width="800" alt="Video demo de la aplicación">
</p>

> [!TIP] 
> **La aplicación está disponible en línea** Puedes ver una demostración en vivo aquí: [**crypto-price-visualizer-one.vercel.app**](https://crypto-price-visualizer-one.vercel.app/)

## Objetivo Final
Este proyecto es una **aplicación web simple** que muestra, en tiempo real, los precios de las 10 principales criptomonedas (por ejemplo, Bitcoin, Ethereum, etc.) en dólares estadounidenses (USD). Su propósito es ofrecer una herramienta accesible para que cualquier persona interesada en el mundo de las criptomonedas pueda visualizar datos actualizados, a la vez que sirve como ejemplo práctico para aprender a integrar APIs en proyectos web utilizando Python.

La interfaz es minimalista y directa, presentando una lista de criptomonedas junto con sus precios actuales, nombres y símbolos. Está diseñada tanto para usuarios sin experiencia técnica como para desarrolladores que deseen explorar el código.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de contar con lo siguiente:

- **Python 3.x**
    
    Descárgalo desde [python.org](https://www.python.org/downloads/) si no lo tenes instalado.
    
- **Clave API de CoinMarketCap**
    
    Registrate en [CoinMarketCap API](https://coinmarketcap.com/api/) para obtener una clave API gratuita, necesaria para acceder a los datos de las criptomonedas.
    

## Configuración del Proyecto

Sigue estos pasos para preparar el proyecto en tu computadora:

1. **Clonar el Repositorio**
    
    
2. **Instalar las Dependencias**
    
    El proyecto utiliza algunas bibliotecas de Python. Instálalas con:
    
    ```bash
    pip install -r requirements.txt
    ```
    
    **Recomendación:** Utiliza un entorno virtual:
    
    ```bash
    python -m venv venv

    venv\Scripts\activate  # En Windows
    ```
    
3. **Configurar la Clave API**
    - Crea un archivo llamado `.env` en la raíz del proyecto.
    - Agrega tu clave API en el siguiente formato:
        
        ```
        CMC_API_KEY=tu_clave_api
        ```
        

## Cómo Ejecutar el Proyecto

Para ver la aplicación en acción, sigue estos pasos:

1. **Iniciar la Aplicación**
    
    Ejecuta en la terminal:
    
    ```bash
    python app.py
    ```
    
    Esto lanzará un servidor local utilizando Flask.
    
2. **Acceder a la Aplicación**
    
    Abre tu navegador web y visita:
    
    ```
    http://localhost:5000
    ```
        

## Estructura del Proyecto
```
CMC-price/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html         # Página principal (precios)
│   ├── noticias.html      # Página de noticias
│   └── mercado.html       # Página de estadísticas del mercado
│
├── app.py                 # Aplicación Flask principal
├── .env                   # Archivo de configuración (no incluido en el repositorio)
├── requirements.txt       # Dependencias del proyecto
├── Procfile               # Configuración para despliegue en Heroku
└── README.md
``` 


## Solución de Problemas

> ⚠️ **Problemas Comunes**:
> 
> - _Error "401 Unauthorized"_
>     
>     Verifica que la clave API esté correctamente configurada en el archivo `.env` o en las variables de entorno del servicio de hosting y que sea válida.
>     
> - _Error "429 Too Many Requests"_
>     
>     Has superado el límite gratuito de 333 solicitudes diarias. Espera hasta el día siguiente o considera un plan de pago en CoinMarketCap.
>     
> - _La página no carga_
>     
>     Asegúrate de que el servidor esté corriendo y que estés utilizando la URL correcta.
>     
> - _Error en el despliegue_
>     
>     Verifica los logs del servicio de hosting para identificar el problema específico.
>     

<br></br>
> [!WARNING]
> El proyecto utiliza el plan gratuito de CoinMarketCap, que tiene limitaciones (333 solicitudes diarias y 10,000 mensuales)
