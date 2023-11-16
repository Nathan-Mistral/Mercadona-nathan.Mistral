from django.test import TestCase
from django.urls import reverse
from .models import Categorie, Produit
from .views import load_catalogue_page, creer_produit, creer_categorie, supprimer_categorie, connexion, deconnexion, supprimer_produit, load_filtre_page, ajouter_promo
from .forms import CategorieForm 



class TestCaseViews(TestCase):
    #Test views Load Catalogue Page
    def test_load_catalogue_page(self):
        url = reverse(load_catalogue_page)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/catalogue.html')        

    #Test views Creer Produit
    def test_creer_produit(self):
        url = reverse(creer_produit)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        template_used = response.templates[0].name
        self.assertEqual(template_used, 'catalogue/ajout_produit.html')


    # Test Views Creer Categorie 
    def test_creer_categorie(self):
        url = reverse(creer_categorie)  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        template_used = response.templates[0].name
        self.assertEqual(template_used, 'catalogue/ajout_categorie.html')   
    
    def test_sauvgarder_categorie(self):
        data = {'nom': 'Test_categorie'}
        formulaire = CategorieForm(data)
        
        self.assertTrue(formulaire.is_valid())
        url = reverse(creer_categorie)  

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)   
        template_used = response.templates[0].name
        self.assertEqual(template_used, 'catalogue/catalogue.html')   

    def test_sauvgarder_categorie_invalide(self):
        data = { }
        formulaire = CategorieForm(data)
        
        self.assertFalse(formulaire.is_valid())
        url = reverse(creer_categorie)  

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)   
        template_used = response.templates[0].name
        self.assertEqual(template_used, 'catalogue/ajout_categorie.html')   


    #Test Views Supprimer Catégorie
    def test_load_supprimer_categorie(self):
        url = reverse(supprimer_categorie)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/sup_categorie.html')

    def test_supprimer_categorie(self):
        self.categorie = Categorie.objects.create(nom="Test Catégorie")
        url = reverse(supprimer_categorie)  
        data= {'categorie_id': self.categorie.id}
        
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, 302)   


    # Test Views Connexion
    def test_load_connexion(self):
        url = reverse(connexion)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/connexion.html')

    def test_connexion_KO(self):
        url = reverse(connexion)  
        data= {'username':'marche_pas', 'password':'12345'}
        
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/connexion.html')


    #Test views Load Deconnexion
    def test_deconnexion(self):
        url = reverse(deconnexion)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/catalogue.html')


    #Test views Supprimer Produit
    def test_load_supprimer_produit(self):
        url = reverse(supprimer_produit)  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/sup_produit.html')

    #Test views Load Filtre Page 
    def test_load_filtre_page(self):
        filtre_categorie_id=1
        url = reverse( load_filtre_page, kwargs={'filtre_categorie_id': filtre_categorie_id})  

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)   
        
        template_used = response.templates[0].name
        self.assertEqual(template_used , 'catalogue/catalogue.html')


    
    
    




        
    
        
    
    

