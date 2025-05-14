from django.contrib import admin
from .models import Produit
from .models import Facture


admin.site.register(Produit)
admin.site.register(Facture)
