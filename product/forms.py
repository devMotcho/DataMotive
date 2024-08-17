from django import forms
from .models import Category, Product, Measurement


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('ref',)

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'