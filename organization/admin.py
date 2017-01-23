from django.contrib import admin

from . import models

@admin.register(models.Responsability_type)
class Responsability_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Responsability)
class ResponsabilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'end_date')
    filter_horizontal = ('identities',)
