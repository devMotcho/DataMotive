from django.contrib import admin
from .models import Client, Supplier, ClientType, SupplierType
admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(ClientType)
admin.site.register(SupplierType)
