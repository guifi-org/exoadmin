from django.contrib import admin

from . import models

@admin.register(models.Identity)
class IdentifiedAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')
    list_filter = ('user_type',)
