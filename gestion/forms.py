from django import forms
from .models import Produit
from .models import Facture

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['id', 'nom', 'prix', 'date_peremption']
    
    def clean_id(self):
        id = self.cleaned_data.get('id')
        if not id.isdigit():
            raise forms.ValidationError("L'ID doit être un nombre entier positif.")
        if int(id) <= 0:
            raise forms.ValidationError("L'ID doit être supérieur à 0.")
        return id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['id'].disabled = True

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['id', 'produits']

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if not id.isdigit():
            raise forms.ValidationError("L'ID doit être un nombre entier positif.")
        if int(id) <= 0:
            raise forms.ValidationError("L'ID doit être supérieur à 0.")
        return id
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['id'].disabled = True
