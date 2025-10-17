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
    
    if request.reset:
        chat_service.reset_chat()
        
        role_lower = request.role.lower()
        
        try:
            chat_service.set_role(RolePreset(role_lower))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        try:
            response = chat_service.send_message(request.mensaje)
            return ChatResponse(respuesta=response)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error al procesar el mensaje.")