from django import forms

from .models import Supplier, Client, EntityType

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ('supplier_id',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('client_id',)

class EntityTypeForm(forms.ModelForm):
    class Meta:
        model = EntityType
        fields = '__all__'