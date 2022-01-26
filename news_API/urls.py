from django.urls import path
from . import views

urlpatterns = [
    path('refresh',views.refresh),
    path('newsList',views.newsList)
]
