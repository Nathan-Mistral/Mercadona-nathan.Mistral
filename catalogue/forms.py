from django import forms
from .models import Categorie, Produit, Promotion



#Permet de gérer les connection
class LoginForm(forms.Form):
    username = forms.CharField( label='Nom d’utilisateur')
    password = forms.CharField( widget=forms.PasswordInput, label='Mot de passe')


#Permet de gérer les création (Produit et Catégorie)
class ProduitForm(forms.ModelForm): 
   class Meta:
      model = Produit
      fields = ['nom', 'prix', 'description', 'categorie','image']

class CategorieForm(forms.ModelForm): 
   class Meta:
      model = Categorie
      fields = ['nom']


#Permet de gérer les supprésion (Produit et Catégorie)
class SupProduit (forms.Form):
    product_id = forms.ModelChoiceField(queryset=Produit.objects.all())

class SupCategorie (forms.Form):
    categorie_id = forms.ModelChoiceField(queryset=Categorie.objects.all())


#Permet de mettre une promotion sur un Produit
class PromoForm (forms.ModelForm):
    class Meta:
      model = Promotion
      fields = ['produit','date_debut', 'date_fin', 'pourcentage_promo']
    
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin and date_debut > date_fin:
            raise forms.ValidationError("La date de début ne peut pas être après la date de fin.")

    def get_global_error(self):
        errors = self.errors.get('__all__')
        if errors == None:
           return('')
        else: 
           return(errors)