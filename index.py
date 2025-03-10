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
      "src": "/favicon.ico",
      "dest": "/static/favicon.ico"
    },
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}

from app import app
import os

# Para Vercel
if __name__ == "__main__":
    app.run()

@app.route("/")
def inicio():
    try:
        # Tu código existente
        clave_api = os.getenv("CMC_API_KEY")
        if not clave_api:
            return render_template("index.html", error="Clave API no configurada")
            
        # Resto del código...
    except Exception as e:
        return render_template("index.html", error=f"Error: {str(e)}")
