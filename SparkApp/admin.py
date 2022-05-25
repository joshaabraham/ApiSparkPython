from django.contrib import admin
from .modelsBo import * 
from django.contrib.auth.admin import UserAdmin

admin.site.register(SparkUser, UserAdmin)

# Register your models here.
admin.register(Produit)

