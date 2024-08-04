from django import forms
from transactions.models import Sale, Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ('transaction_id',)


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ('transaction_id',)
