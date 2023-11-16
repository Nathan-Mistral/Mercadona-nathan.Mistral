from django.db import models
from django.utils import timezone
from decimal import Decimal
from datetime import datetime
from django import forms



# définie la class Catégorie
class Categorie (models.Model):
    nom = models.CharField(max_length=100)
   
    
    def __str__(self) :
        return self.nom


# Définie la class  Produit 
class Produit (models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0.0)
    description= models.CharField(max_length=200)
    categorie= models.ForeignKey (Categorie, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produit', null=True)
    date_added= models.DateTimeField(auto_now=True,)
    

    class Meta: 
        ordering = ['-date_added']
    
    def __str__(self) :
        return self.nom
    
    @property
    def est_en_promotion(self):
        promo= False
        if self.promotions.all():
            for promotion in self.promotions.all():
                if promotion.est_activee and not promotion.est_expiree:
                    promo = True
                    break
        else:
            promo = False
        return promo

#Définie la class Promotion
class Promotion (models.Model):
    produit= models.ForeignKey( Produit, related_name='promotions', on_delete=models.CASCADE, null=True )   
    date_debut = models.DateField(blank=True)
    date_fin = models.DateField( blank=True)
    pourcentage_promo= models.PositiveIntegerField(default=0.0, null= True)
    prix_promo = models.FloatField(default=0.0, blank=True)
    
    
    def calcul_nouveau_prix (self):
        if self.produit: 
            reduction= self.produit.prix * (self.pourcentage_promo/100)
            self.prix_promo = self.produit.prix - reduction
    
    def save(self, *args, **kwargs):
        self.calcul_nouveau_prix()
        super(Promotion, self).save(*args, **kwargs)
    
    @property
    def est_expiree (self):
        if self.date_fin < timezone.now().date():
            return True
        else:
            return False
    
    @property
    def est_activee(self):
        if self.date_debut <= timezone.now().date():
            return True
        else:
            return False

