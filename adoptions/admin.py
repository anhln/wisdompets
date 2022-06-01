from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'submitter', 'description']

admin.site.register(Pet,PetAdmin)