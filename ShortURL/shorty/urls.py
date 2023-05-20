from django.urls import path
from . import views
from .models import URL

urlpatterns = [
    path('',  views.shortlink, name='shortlink'),
    path('shorty/', views.shorty_home, name='shorty_home'),
    path('<int:pk>', views.ShortyDetailView.as_view(), name='shortlink-detail'),
    path('<int:pk>/delete', views.ShortyDeleteView.as_view(), name='shortlink-delete'),
    path('<int:pk>/shutdown', views.shutdown, name='shutdown')
]
