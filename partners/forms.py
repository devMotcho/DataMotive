from django import forms

from .models import Supplier, Client, EntityType
from src.validators import validate_unique_name

def validate_unique_name_client(value):
    validate_unique_name(value, Client, 'name')
def validate_unique_name_supplier(value):
    validate_unique_name(value, Supplier, 'name')


class SupplierForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_unique_name_supplier])
    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ('supplier_id',)


class ClientForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_unique_name_client])
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('client_id',)

class EntityTypeForm(forms.ModelForm):
    class Meta:
        model = EntityType
        fields = '__all__'