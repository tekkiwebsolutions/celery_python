"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from starlette.routing import Mount
from starlette.applications import Starlette
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import URLRouter, ProtocolTypeRouter
from fastapi import APIRouter, FastAPI, WebSocket

# local imports
from websocket.routing import websocket_urlpatterns


router = APIRouter()


# simple api
@router.get("/hello/")
async def read_users():
    return 'hello'


from websocket.utils import get_task_result


# websocket api
@router.websocket("/fast-ws/{task_id}/")
async def websocket_endpoint(websocket: WebSocket, task_id: str):
    await websocket.accept()
    print('hehe')
    await websocket.send_text("Hello WebSocket")
    await get_task_result(task_id, websocket)
    await websocket.close() 


app = FastAPI()

app.include_router(router)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)

# Wrap the FastAPI app using Starlette's Mount to make it ASGI-compatible
combined_app = Starlette(
    routes=[
        Mount("/fastapi", app),
        Mount("/", application),  # Mount the combined ASGI app under a common path
    ]
)
