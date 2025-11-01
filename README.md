# 🚀 Chatbot Gemini Completo

> **✅ PROYECTO COMPLETAMENTE FUNCIONAL**  
> Backend FastAPI + Frontend React + Google Gemini AI

Un chatbot inteligente completo con interfaz moderna que utiliza la API de Google Gemini para proporcionar conversaciones contextuales con diferentes roles especializados.

![Status](https://img.shields.io/badge/Status-✅%20Funcionando-brightgreen)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-4285F4)

## 🎯 Instrucciones para el Profesor

### ⚡ Inicio Rápido (30 segundos)

1. **Clona el repositorio** y navega al directorio:
   ```bash
   git clone https://gitlab.com/modelado_de_soft/chatbot-gemini-completo.git
   cd chatbot-gemini-completo
   ```

2. **Configura la API Key** de Google Gemini:
   ```bash
   # Copia el archivo de ejemplo
   cp .env.example .env
   
   # Edita el archivo .env y reemplaza 'demo-key-placeholder' con tu API key real
   # Obtén tu API key en: https://makersuite.google.com/app/apikey
   ```

3. **Instala y ejecuta el Backend**:
   ```bash
   # Crear entorno virtual
   python -m venv venv
   
   # Activar entorno virtual (Windows)
   venv\Scripts\activate
   # En Linux/macOS: source venv/bin/activate
   
   # Instalar dependencias
   pip install -r requirements.txt
   
   # Ejecutar servidor
   uvicorn main:app --reload
   ```

4. **Instala y ejecuta el Frontend** (nueva terminal):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

5. **¡Listo!** 🎉
   - Backend: http://127.0.0.1:8000
   - Frontend: http://localhost:5173
   - Documentación API: http://127.0.0.1:8000/docs
- Clave API de Google Gemini
- Dependencias listadas en `requirements.txt`

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/NataliaAraujo24/mi-chatbot-gemini.git
cd mi-chatbot-gemini
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

5. Configura tu clave API:
   - Copia el archivo `.env.example` a `.env`
   - Agrega tu clave API de Gemini en el archivo `.env`:
```
GEMINI_API_KEY=tu-clave-api-aqui
MODEL=gemini-pro-latest
MAX_RETRIES=3
TIMEOUT_SECONDS=30
MAX_HISTORY=12
```

## 🎮 Uso

Ejecuta el chatbot:
```bash
python main.py
```

### Comandos Disponibles

- `:rol [profesor|traductor|programador|asistente]` - Cambia el rol del chatbot
- `:reset` - Limpia la memoria de conversación
- `:salir` - Termina la aplicación

## 📁 Estructura del Proyecto

```
chatbot-gemini/
│
├── main.py              # Archivo principal de la aplicación
├── chat_service.py      # Servicio principal del chatbot
├── llm_client.py        # Cliente para la API de Gemini
├── config.py            # Configuración y variables de entorno
├── roles.py             # Definición de roles y prompts
├── prompts.py           # Manejo de prompts del sistema
├── memory.py            # Gestión de memoria conversacional
├── requirements.txt     # Dependencias del proyecto
├── .env                 # Variables de entorno (no incluido en el repo)
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo
```

## 🔑 Obtener una API Key de Gemini

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Cópiala y agrégala a tu archivo `.env`

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**NataliaAraujo24**
- GitHub: [@NataliaAraujo24](https://github.com/NataliaAraujo24)

---
⭐ ¡Si te gusta este proyecto, dale una estrella en GitHub!# mi-chatbot-gemini1
