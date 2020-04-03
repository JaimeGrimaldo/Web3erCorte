from django.urls import path
from .views import RegistrateView

app_name = 'Registro'

urlpatterns = [
    path('',RegistrateView.as_view(),name = 'registro' ),
]
