from django.db import models


class Produit(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return f"[{self.id}] {self.nom}, {self.prix}€ - {self.date_peremption}"


class Facture(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit, related_name='factures')

    def total(self):
        return sum(produit.prix for produit in self.produits.all())

    def __str__(self):
        return f"Facture {self.id}"
