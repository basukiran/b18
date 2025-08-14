from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL handled by the home view
]