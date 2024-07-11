from django.urls import path
from .views import(
    loginPage,
    logoutUser,
)
app_name = 'authentic'

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
]