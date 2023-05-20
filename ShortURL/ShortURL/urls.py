"""
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from shorty.views import root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shorty.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('<str:url_hash>/', root, name='root'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
