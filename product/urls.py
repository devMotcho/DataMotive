from django.urls import path
from .views import (
    productTable,
)
app_name = 'product'

urlpatterns = [
    path('', productTable, name='table'),
]