from django import forms

from .models import Supplier, Client, EntityType

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EntityTypeForm(forms.ModelForm):
    class Meta:
        model = EntityType
        fields = '__all__'