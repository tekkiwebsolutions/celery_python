from asgiref.sync import sync_to_async, async_to_sync
from asyncio import sleep as async_sleep
from celery.result import AsyncResult
import json
from channels.layers import get_channel_layer
from fastapi import WebSocket

async def send_message_to_websocket(channel_name: str, message: dict):
    print(f"==>> channel_name: {channel_name}")
    print('RRRRRRRRR')
    channel_layer = get_channel_layer()
    print(type(channel_layer))
    await channel_layer.group_send(channel_name, {
            "type": "custom_message",
            "message": json.dumps({'status': 'PENDINGGGGG'})})
    


@sync_to_async
def get_task_state(task_id):
    return AsyncResult(task_id).state


@sync_to_async
def get_task_details(task_id):
    state = AsyncResult(task_id).state
    result = AsyncResult(task_id).result
    return {'state': state, 'result': result}


async def get_task_result(task_id, channel):
    while await get_task_state(task_id) == 'PENDING':
        print(1)
        await async_sleep(1)
        print(f"==>> chanel_name: {channel}")
        if isinstance(channel, WebSocket):
            await channel.send_text(json.dumps({'status': 'Fast'}))
        else:
            await send_message_to_websocket(
                task_id, {'status': 'PENDINGGGGG'})
    task = await get_task_details(task_id)
    print(task['state']*50)
    if isinstance(channel, WebSocket):
        await channel.send_text(json.dumps(
            {'status': task['state'], 'result': task['result']}))
    else:
        await send_message_to_websocket(
            task_id, {'status': task['state'], 'result': task['result']})
    # yield
    # await self.send(text_data=json.dumps(
    #     {'status': task['state'], 'result': task['result']}
    # ))
