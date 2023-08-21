from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import get_task_result, send_message_to_websocket
import asyncio


class TaskStatusConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        task_id = self.scope['url_route']['kwargs']['task_id']
        self.task_group_name = task_id
        await self.channel_layer.group_add(self.task_group_name, self.channel_name)
        await self.accept()
        print('connected')
        await get_task_result(task_id, self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.task_group_name, self.channel_name)
        print('close_code', close_code)
        print('disconnected')

    async def receive(self, text_data):
        pass

    async def custom_message(self, event):
        message = event['message']
        print('$$$$$$$$$$$$')
        await self.send(text_data=message)
        print('message', message)
