# """
# ASGI config for project project.
#
# It exposes the ASGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
# """
from django.core.asgi import get_asgi_application
# django_asgi_app = get_asgi_application()
#
# import os
# from django.conf.urls import url
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
#
# django_asgi_app = get_asgi_application()
# from apps.chat import routing
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
#
# application = ProtocolTypeRouter({
#   "http": django_asgi_app,
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })






import os
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
from project.middlewares import TokenAuthMiddlewareStack
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import apps.real_time.routing as routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = ProtocolTypeRouter({
  "https": django_asgi_app,
  "websocket": TokenAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
