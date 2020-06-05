import asyncio
import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer


class GeoTrackConsumer(WebsocketConsumer):
    def connect(self, event):
        print('connected', event)

    def receive(self, event):
        print('receive', event)

    def disconnect(self, event):
        print('disconnectd', event)


class PingConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': text_data
        }))

    def disconnect(self, close_code):
        print('disconnected', close_code)
