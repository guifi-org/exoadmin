from django.contrib import admin

from . import models

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('identity', 'service', 'active')
    list_filter = ('active', 'service')
