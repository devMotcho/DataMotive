from django.urls import path
from .views import (
    partnersTable,
    partnersDelete,
    partnersDetail,
)
app_name = 'partners'

urlpatterns = [
    path('', partnersTable, name='table'),
    path('delete/<str:pk>/', partnersDelete, name='delete'),
    path('<str:pk>', partnersDetail, name='detail'),
]