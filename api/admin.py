from django.contrib import admin
from api.models import Hero, Prodect, ProdectImage,Catecory

# Register your models here.
admin.site.register(Prodect)
admin.site.register(ProdectImage)
admin.site.register(Catecory)
admin.site.register(Hero)