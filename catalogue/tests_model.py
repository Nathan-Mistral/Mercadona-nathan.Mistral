
from django.test import TestCase
from .models import Produit, Categorie, Promotion
from datetime import datetime, timedelta, date



class TestCaseModel(TestCase):
    
    def setUp(self):
        # Crée une catégorie pour les tests
        self.categorie = Categorie.objects.create(nom="Test Catégorie")
        
        self.date =datetime.now() - timedelta(days=1)
        
        # Crée un produit pour les tests
        self.produit = Produit.objects.create(
            nom="Test Produit",
            prix=20.0,
            description="Ceci est un produit de test",
            categorie= self.categorie,
            image="produit/test_image.jpg",
            date_added= self.date,  
        )
        

    #Test la création d'un produit
    def test_creation_produit(self):
        self.assertEqual(self.produit.nom, "Test Produit")
        self.assertEqual(self.produit.prix, 20.0)
        self.assertEqual(self.produit.description, "Ceci est un produit de test")
        self.assertEqual(self.produit.categorie, self.categorie )
        self.assertEqual(self.produit.image, "produit/test_image.jpg")

    #test la création d'une catégorie 
    def test_creation_categorie(self):
        self.assertEqual(self.categorie.nom, "Test Catégorie")

    



    

    

        

        


