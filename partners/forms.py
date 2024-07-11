from django import forms

from .models import Supplier, Client, SupplierType, ClientType

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SupplierTypeForm(forms.ModelForm):
    class Meta:
        model = SupplierType
        fields = '__all__'

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model = ClientType
        fields = '__all__'
