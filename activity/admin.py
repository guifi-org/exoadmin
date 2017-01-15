from django.contrib import admin

from . import models

@admin.register(models.Type_of_activity)
class Type_of_activity_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    filter_horizontal = ('identities',)
