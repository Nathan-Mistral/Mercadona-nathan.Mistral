"""
URL configuration for mercadona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from catalogue.views import  (load_catalogue_page, load_filtre_page, connexion, deconnexion, 
                              creer_produit, creer_categorie, supprimer_produit, ajouter_promo, supprimer_categorie)
from mercadona import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogue/',  load_catalogue_page,   name="index"),
    path('', load_catalogue_page,  name='acceuil'), 
    path('catalogue/<int:filtre_categorie_id>/', load_filtre_page, name="filtre" ),
   
   
    path('connexion/', connexion, name="connexion"),
    path('deconnexion/', deconnexion, name="deconnexion"),

    path ('ajout-poduit/', creer_produit, name="creer_produit"),
    path ('ajout-categorie/', creer_categorie, name="creer_categorie"),
    path ('ajouter-promo/<int:produit_id>/', ajouter_promo, name="ajouter_promo"),

    path ('suprimer-produit/', supprimer_produit, name="supprimer_produit"),
    path ('suprimer-categorie/', supprimer_categorie, name="supprimer_categorie"),
    
    


    
     
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


