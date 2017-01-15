from django.contrib import admin

from . import models

@admin.register(models.Type_of_responsability)
class Type_of_responsability_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Responsability)
class ResponsabilityAdmin(admin.ModelAdmin):
    filter_horizontal = ('identities',)
