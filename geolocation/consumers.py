import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import AgencyLocation, SalesmanLocationHis


class GeoTrackConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)

    async def websocket_receive(self, event):
        print('receive', event)

    async def websocket_disconnect(self, event):
        print('disconnectd', event)


class PingConsumer(AsyncConsumer):
    async def websocket_connect(self, message):
        print('connected', message)

    async def websocket_receive(self, event):
        print('receive', event)

    async def websocket_disconnect(self, event):
        print('disconnectd', event)
