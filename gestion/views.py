from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import ProduitForm
from django.core.paginator import Paginator
from .models import Facture
from .forms import FactureForm
from django.http import HttpResponse


def liste_produits(request):
    produits = Produit.objects.all().order_by('id')
    paginator = Paginator(produits, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gestion/liste_produits.html', {'page_obj': page_obj})


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'gestion/ajouter_produit.html', {'form': form})


def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'gestion/modifier_produit.html', {'form': form})


def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    produit.delete()
    return redirect('liste_produits')


def liste_factures(request):
    factures = Facture.objects.all().order_by('id')
    paginator = Paginator(factures, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gestion/liste_factures.html', {'page_obj': page_obj})


def ajouter_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_factures')
    else:
        form = FactureForm()
    return render(request, 'gestion/ajouter_facture.html', {'form': form})


def modifier_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('liste_factures')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'gestion/modifier_facture.html', {'form': form})


def supprimer_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    facture.delete()
    return redirect('liste_factures')


def details_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    return render(request, 'gestion/details_facture.html', {'facture': facture})


def telecharger_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    produits = facture.produits.all()
    contenu = f"Facture n°{facture.id}\n"
    contenu += f"Date de création : {facture.date_creation}\n"
    contenu += f"Prix total : {facture.total()}€\n"
    contenu += f"Nombre de produits : {produits.count()}\n\n"
    contenu += "Produits associés :\n"

    for produit in produits:
        contenu += f"- {produit.nom} - {produit.prix}€\n"

    response = HttpResponse(contenu, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="facture_{facture.id}.txt"'
    return response
