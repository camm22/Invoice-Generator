from django.urls import path
from . import views

urlpatterns = [
    # Produits
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),

    # Factures
    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/ajouter/', views.ajouter_facture, name='ajouter_facture'),
    path('factures/<int:facture_id>/', views.details_facture, name='details_facture'),
    path('factures/<int:facture_id>/modifier/', views.modifier_facture, name='modifier_facture'),
    path('factures/<int:facture_id>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
    path('factures/<int:facture_id>/telecharger/', views.telecharger_facture, name='telecharger_facture'),
]
