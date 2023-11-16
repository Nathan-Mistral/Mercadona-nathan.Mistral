from django.contrib import admin
from .models import Produit, Categorie, Promotion
# Register your models here.

admin.site.site_header = "Mercadona"
admin.site.index_title= "Mercadona"


class AdminProduit(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'categorie')
    search_fields= ('nom',)

class AdminPromotion(admin.ModelAdmin):
    list_display=('pourcentage_promo','date_debut','date_fin')



admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie)
admin.site.register(Promotion,AdminPromotion)

