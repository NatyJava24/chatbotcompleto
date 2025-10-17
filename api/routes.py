from fastapi import APIRouter, HTTPException
from api.schemas import ChatRequest, ChatResponse
from chat_service import ChatService
from roles import RolePreset

router = APIRouter()
chat_service = ChatService(role=RolePreset.ASISTENTE)

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.mensaje:
        raise HTTPException(status_code=400, detail="El campo 'mensaje' es obligatorio.")
    
    try:
        # Si reset es True, limpiar la memoria
        if request.reset:
            chat_service.reset()
            
            # Cambiar el rol si se especifica
            role_lower = request.role.lower()
            try:
                chat_service.set_role(RolePreset(role_lower))
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
        # Procesar el mensaje (fuera del bloque reset)
        response = chat_service.ask(request.mensaje)
        return ChatResponse(respuesta=response)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el mensaje: {str(e)}")