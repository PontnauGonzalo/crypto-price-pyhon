# Proyecto: Visualizador de Precios de Criptomonedas con CoinMarketCap API
[![Python](https://img.shields.io/badge/docs-Python-blue?logo=python)](https://docs.python.org/3/)
[![Flask](https://img.shields.io/badge/docs-Flask-green?logo=flask)](https://flask.palletsprojects.com/)
[![CoinMarketCap API](https://img.shields.io/badge/docs-CMC_API-white?logo=coinmarketcap)](https://coinmarketcap.com/api/documentation/v1/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/2a0a3551-c67c-49bb-b032-2249161c3999" width="800" alt="Video demo de la aplicación">
</p>

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

## Despliegue en Servicios de Hosting Gratuitos

Esta aplicación está preparada para ser desplegada en varios servicios de hosting gratuitos. A continuación, se detallan los pasos para algunos de los más populares:

### Render

1. **Crear una cuenta en Render**
   - Regístrate en [render.com](https://render.com/)

2. **Crear un nuevo servicio web**
   - Haz clic en "New" y selecciona "Web Service"
   - Conecta tu repositorio de GitHub o sube el código directamente

3. **Configurar el servicio**
   - **Nombre**: Elige un nombre para tu aplicación
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Configurar variables de entorno**
   - En la sección "Environment", añade la variable `CMC_API_KEY` con tu clave de API de CoinMarketCap

5. **Desplegar**
   - Haz clic en "Create Web Service"
   - Render desplegará automáticamente tu aplicación

### PythonAnywhere

1. **Crear una cuenta en PythonAnywhere**
   - Regístrate en [pythonanywhere.com](https://www.pythonanywhere.com/)

2. **Subir el código**
   - Ve a la sección "Files" y sube todos los archivos del proyecto
   - O clona el repositorio usando la consola de PythonAnywhere

3. **Configurar un entorno virtual**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 myenv
   pip install -r requirements.txt
   ```

4. **Configurar la variable de entorno**
   - Crea un archivo `.env` con tu clave API

5. **Configurar la aplicación web**
   - Ve a la pestaña "Web"
   - Haz clic en "Add a new web app"
   - Selecciona "Manual configuration" y Python 3.8
   - Configura el campo "Source code" a la ruta de tu proyecto
   - Configura el campo "Working directory" a la misma ruta
   - En la sección "WSGI configuration file", edita el archivo para que contenga:
     ```python
     import sys
     path = '/home/tuusuario/ruta-a-tu-proyecto'
     if path not in sys.path:
         sys.path.append(path)
     
     from app import app as application
     ```

6. **Reiniciar la aplicación**
   - Haz clic en el botón "Reload"

### Vercel

1. **Instalar Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Crear archivo vercel.json**
   Crea un archivo `vercel.json` en la raíz del proyecto:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Desplegar**
   ```bash
   vercel
   ```

4. **Configurar variables de entorno**
   - En el dashboard de Vercel, ve a tu proyecto
   - Ve a "Settings" > "Environment Variables"
   - Añade la variable `CMC_API_KEY` con tu clave de API

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
> [!NOTE]
> El proyecto utiliza el plan gratuito de CoinMarketCap, que tiene limitaciones (333 solicitudes diarias y 10,000 mensuales)
