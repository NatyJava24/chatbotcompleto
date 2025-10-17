# 🚀 Chatbot Gemini Completo
## Backend FastAPI + Frontend React Integrados

Un chatbot inteligente completo con interfaz moderna que utiliza la API de Google Gemini para proporcionar conversaciones contextuales con diferentes roles especializados.

![Chatbot Demo](https://img.shields.io/badge/Status-✅%20Funcionando-brightgreen)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-4285F4)

## ✨ Características Principales

### 🤖 **Backend (FastAPI)**
- **4 Roles Especializados**: Profesor, Traductor, Programador, Asistente
- **Memoria Conversacional**: Mantiene el contexto de la conversación
- **API REST**: Endpoints bien documentados
- **Integración Gemini**: Conexión directa con Google Gemini AI
- **CORS Configurado**: Comunicación frontend-backend
- **Manejo de Errores**: Respuestas consistentes y informativas

### 🎨 **Frontend (React + Vite)**
- **Interfaz Moderna**: Diseño responsive con Tailwind CSS
- **Chat en Tiempo Real**: Comunicación fluida con el backend
- **Selector de Roles**: Cambio dinámico de personalidad del asistente
- **Estados de Carga**: Feedback visual durante las respuestas
- **Animaciones Suaves**: Transiciones fluidas y atractivas
- **Compatible Móvil**: Experiencia optimizada para todas las pantallas

## 🎭 Roles Disponibles

| Rol | Icono | Descripción |
|-----|-------|-------------|
| **Profesor** | 👨‍🏫 | Explica conceptos de manera didáctica y clara |
| **Traductor** | 🌍 | Traduce textos entre idiomas manteniendo contexto |
| **Programador** | 💻 | Ayuda con código, debugging y mejores prácticas |
| **Asistente** | 🤖 | Asistente general para diversas tareas |

## 🛠️ Tecnologías Utilizadas

### Backend
- **FastAPI** - Framework web moderno y rápido
- **Google Gemini AI** - Modelo de inteligencia artificial
- **Python 3.7+** - Lenguaje de programación
- **Pydantic** - Validación de datos
- **CORS Middleware** - Comunicación cross-origin

### Frontend
- **React 18** - Biblioteca de interfaz de usuario
- **Vite** - Herramienta de desarrollo rápida
- **Tailwind CSS** - Framework de estilos utility-first
- **Lucide React** - Iconos modernos y consistentes
- **JavaScript ES6+** - Lenguaje de programación moderno

## 📋 Requisitos

- **Python 3.7+**
- **Node.js 16+** y **npm**
- **Clave API de Google Gemini**
- **Git** para clonar el repositorio

## 🚀 Instalación y Configuración

### 1. **Clonar el Repositorio**
```bash
git clone https://gitlab.com/modelado_de_soft/chatbot-gemini-completo.git
cd chatbot-gemini-completo
```

### 2. **Configurar Backend**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. **Configurar Variables de Entorno**
Crea un archivo `.env` en la raíz del proyecto:
```env
GEMINI_API_KEY=tu-clave-api-aqui
MODEL=gemini-pro
MAX_RETRIES=3
TIMEOUT_SECONDS=30
MAX_HISTORY=12
```

### 4. **Configurar Frontend**
```bash
cd frontend
npm install
```

## 🎮 Uso

### **Ejecutar Backend**
```bash
# Desde la raíz del proyecto
uvicorn main:app --reload
```
- 🌐 **API**: http://127.0.0.1:8000
- 📚 **Documentación**: http://127.0.0.1:8000/docs

### **Ejecutar Frontend**
```bash
# Desde la carpeta frontend
cd frontend
npm run dev
```
- 🌐 **Interfaz**: http://localhost:5173 (o puerto disponible)

### **Usar la Aplicación**
1. **Abre el frontend** en tu navegador
2. **Selecciona un rol** (Profesor, Traductor, Programador, Asistente)
3. **Escribe tu mensaje** en el chat
4. **Disfruta** de las respuestas inteligentes
5. **Cambia roles** o **resetea** la conversación cuando quieras

## 📁 Estructura del Proyecto

```
chatbot-gemini-completo/
│
├── 🔧 Backend (FastAPI)
│   ├── main.py              # Aplicación principal
│   ├── chat_service.py      # Servicio del chatbot
│   ├── llm_client.py        # Cliente Gemini AI
│   ├── config.py            # Configuración
│   ├── roles.py             # Definición de roles
│   ├── prompts.py           # Manejo de prompts
│   ├── memory.py            # Memoria conversacional
│   ├── requirements.txt     # Dependencias Python
│   ├── .env                 # Variables de entorno
│   └── api/
│       ├── routes.py        # Rutas de la API
│       └── schemas.py       # Esquemas de datos
│
├── 🎨 Frontend (React)
│   ├── src/
│   │   ├── App.jsx          # Componente principal
│   │   ├── main.jsx         # Punto de entrada
│   │   ├── index.css        # Estilos globales
│   │   └── components/
│   │       ├── Header.jsx         # Cabecera
│   │       ├── RoleSelector.jsx   # Selector de roles
│   │       ├── ChatContainer.jsx  # Contenedor del chat
│   │       ├── MessageBubble.jsx  # Burbujas de mensajes
│   │       └── MessageInput.jsx   # Input de mensajes
│   ├── package.json         # Dependencias Node.js
│   ├── vite.config.js       # Configuración Vite
│   ├── tailwind.config.js   # Configuración Tailwind
│   └── postcss.config.js    # Configuración PostCSS
│
└── 📚 Documentación
    └── README.md            # Este archivo
```

## 🔑 Obtener una API Key de Gemini

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Cópiala y agrégala a tu archivo `.env`

## 🌟 Características Avanzadas

- **💾 Persistencia de Memoria**: Las conversaciones mantienen contexto
- **🔄 Reset Inteligente**: Limpia memoria al cambiar roles
- **⚡ Respuestas Rápidas**: Optimizado para velocidad
- **📱 100% Responsive**: Funciona en todos los dispositivos
- **🎨 Interfaz Intuitiva**: Diseño moderno y fácil de usar
- **🛡️ Manejo de Errores**: Recuperación elegante de fallos
- **🔧 Configuración Flexible**: Parámetros ajustables

## 🤝 Contribuir

1. **Fork** del proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autores

**Equipo Modelado de Software**
- GitHub: [@modelado_de_soft](https://gitlab.com/modelado_de_soft)

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitLab!**

🚀 **¡Tu chatbot inteligente está listo para conquistar el mundo!** 🌍✨