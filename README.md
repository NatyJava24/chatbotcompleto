# 🤖 Chatbot Gemini

Un chatbot inteligente desarrollado en Python que utiliza la API de Google Gemini para proporcionar conversaciones contextuales con diferentes roles especializados.

## ✨ Características

- **Múltiples Roles**: Profesor, Traductor, Programador y Asistente
- **Memoria Conversacional**: Mantiene el contexto de la conversación
- **Interfaz Simple**: Fácil de usar desde la línea de comandos
- **Configuración Flexible**: Parámetros ajustables para reintentos y límites

## 🔧 Roles Disponibles

1. **Profesor** 📚 - Explica conceptos de manera didáctica
2. **Traductor** 🌍 - Traduce textos entre idiomas
3. **Programador** 💻 - Ayuda con código y programación
4. **Asistente** 🤝 - Asistente general para diversas tareas

## 📋 Requisitos

- Python 3.7+
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
