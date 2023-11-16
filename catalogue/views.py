from django.shortcuts import render, redirect
from .models import Categorie
from .forms import ProduitForm, CategorieForm, LoginForm, PromoForm
from django.shortcuts import render
from .models import Produit, Promotion
from django.contrib.auth import  login, logout, authenticate




#permet d'afficher les produit sur la page catalogue 
def load_catalogue_page(request):
    categories= Categorie.objects.all()
    produit_objet = Produit.objects.all()
    
    item_name= request.GET.get('item-name')
    if item_name != '' and item_name is not None: 
        produit_objet = Produit.objects.filter(nom__icontains= item_name)

    return render(request, 'catalogue/catalogue.html', {'categories': categories, 'produit_objet': produit_objet })


# permet de gérer la barre de recher par nom des produits
def load_filtre_page (request,filtre_categorie_id):
    categories= Categorie.objects.all()
    produit_objet = Produit.objects.all()

    produit_objet= produit_objet.filter( categorie_id = filtre_categorie_id )
    
    
    item_name= request.GET.get('item-name')
    if item_name != '' and item_name is not None: 
        produit_objet = produit_objet.filter(nom__icontains= item_name)
    
    

    return render(request, 'catalogue/catalogue.html', {'categories': categories, 'produit_objet': produit_objet })


#Permet de gérer les connexion et déconnexion 
def connexion (request):
    categories= Categorie.objects.all()
    produit_objet = Produit.objects.all()

    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user =  authenticate( username= form.cleaned_data['username'],password= form.cleaned_data['password'] )
        if user is not None :
            login(request, user)
            return render(request, 'catalogue/catalogue.html', {'categories': categories, 'produit_objet': produit_objet })
        else : 
            return render(request, 'catalogue/connexion.html', { 'categories': categories } )
    else : 
        return render(request, 'catalogue/connexion.html', { 'categories': categories } )

def deconnexion (request):
    categories= Categorie.objects.all()
    logout (request)
    return render(request, 'catalogue/catalogue.html', { 'categories': categories } )


#Permet de gérer les créarion (Produit, Catégorie et promotion)
def creer_produit(request):
    categories= Categorie.objects.all()
    if request.method =='POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form= ProduitForm()
    
    return render(request, 'catalogue/ajout_produit.html', {'categories': categories,'form':form})

def creer_categorie(request):
    categories= Categorie.objects.all()
    if request.method =='POST':
        form = CategorieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'catalogue/catalogue.html', {'categories': categories,})
    else: 
        form= CategorieForm()
    
    return render(request, 'catalogue/ajout_categorie.html', {'categories': categories,'form':form,})

def ajouter_promo (request,produit_id):
    categories= Categorie.objects.all()
    produit = Produit.objects.all().get(id= produit_id)

    

    if request.method =='POST':
        form = PromoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form= PromoForm()
    
    return render(request, 'catalogue/ajout_promotion.html', {'categories': categories, 'produit':produit,'form':form})


#Permet de gérer les supprésion (Produit et Catégorie)
def supprimer_produit (request):
    categories= Categorie.objects.all()
    produits = Produit.objects.all()
    
    if request.method =='POST':
        product_id = request.POST.get("product_id")
        produit= produits.get(id= product_id)
        produit.delete()
        return redirect('index')

    
    return render(request, 'catalogue/sup_produit.html',{'categories': categories, 'produits': produits} )

def supprimer_categorie (request):
    categories= Categorie.objects.all()
    
    if request.method =='POST':
        categorie_id = request.POST.get("categorie_id")
        categorie= categories.get(id= categorie_id)
        categorie.delete()
        return redirect('index')

    
    return render(request, 'catalogue/sup_categorie.html',{'categories': categories} )
