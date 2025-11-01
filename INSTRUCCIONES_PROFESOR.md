📧 **INSTRUCCIONES PARA EL PROFESOR**

Estimado Profesor,

He completado el proyecto del Chatbot con Gemini AI. Aquí están las instrucciones para ejecutarlo:

## 🚀 ACCESO AL PROYECTO

**Repositorio GitLab:** https://gitlab.com/modelado_de_soft/chatbot-gemini-completo

## ⚡ INSTALACIÓN RÁPIDA (5 minutos)

### 1. Clonar el proyecto:
```bash
git clone https://gitlab.com/modelado_de_soft/chatbot-gemini-completo.git
cd chatbot-gemini-completo
```

### 2. Obtener API Key de Google Gemini (GRATIS):
- Ir a: https://makersuite.google.com/app/apikey
- Iniciar sesión con cuenta de Google
- Crear nueva API Key
- Copiar la clave

### 3. Configurar API Key:
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env y reemplazar 'demo-key-placeholder' con su API key real
```

### 4. Instalar Backend:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 5. Instalar Frontend:
```bash
cd frontend
npm install
cd ..
```

### 6. Ejecutar Aplicación:

**Terminal 1 - Backend:**
```bash
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 7. Acceder al Chatbot:
- **Frontend:** http://localhost:5173
- **API Docs:** http://127.0.0.1:8000/docs

## ✅ FUNCIONALIDADES A PROBAR

1. **Selector de Roles**: 4 roles especializados
   - 👨‍🏫 Profesor: "¿Qué es la fotosíntesis?"
   - 🌍 Traductor: "Traduce 'Hello world' al español"
   - 💻 Programador: "¿Cómo crear una función en Python?"
   - 🤖 Asistente: "¿Cuál es la capital de Francia?"

2. **Memoria Conversacional**: Mantiene contexto de la conversación
3. **Reset de Conversación**: Al cambiar roles
4. **Interfaz Responsive**: Funciona en móvil y desktop

## 🛠️ TECNOLOGÍAS IMPLEMENTADAS

- **Backend:** FastAPI + Python + Google Gemini AI
- **Frontend:** React + Vite + Tailwind CSS
- **API:** REST con documentación automática
- **IA:** Google Gemini 2.5-flash (último modelo)

## 📊 CARACTERÍSTICAS TÉCNICAS

✅ Backend FastAPI completo con 4 endpoints
✅ Frontend React moderno y responsive  
✅ Integración real con Google Gemini AI
✅ 4 roles especializados únicos
✅ Memoria conversacional funcional
✅ Manejo de errores y estados de carga
✅ Documentación completa de API
✅ CORS configurado correctamente

---

**Tiempo estimado de instalación:** 5-10 minutos
**Estado:** ✅ Completamente funcional

Saludos,
[Tu nombre]