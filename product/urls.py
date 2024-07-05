from django.urls import path
from .views import (
    productTable,
    productDetail,
    productDelete,

    categoryTable,
    categoryDetail,
    categoryDelete,
)
app_name = 'product'

urlpatterns = [
    # products
    path('', productTable, name='table'),
    path('detail/<str:pk>/', productDetail, name='detail'),
    path('delete/<str:pk>/', productDelete, name='delete'),

    #categories
    path('categories/', categoryTable, name='categories'),
    path('category/<str:pk>/', categoryDetail, name='category'),
    path('category/delete/<str:pk>/', categoryDelete, name='category-delete'),
]