from django.contrib import admin

from . import models

@admin.register(models.Activity_type)
class Activity_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    filter_horizontal = ('identities',)
