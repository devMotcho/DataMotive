from django.urls import path
from .views import (
    stockInfo,
)
app_name = 'stock'

urlpatterns = [
    path('', stockInfo, name='info'),
]