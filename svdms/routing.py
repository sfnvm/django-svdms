from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from geolocation.consumers import GeoTrackConsumer, PingConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r"ping/$", PingConsumer)
    ])
})
