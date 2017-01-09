from django.contrib import admin

from . import models

admin.site.register(models.Municipality)

@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality')
