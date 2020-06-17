from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .channelsmiddleware import TokenAuthMiddleware
# from apps.geolocation.consumers import PingConsumer


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter([
            # url(r"ping/$", PingConsumer)
        ])
    )
})
