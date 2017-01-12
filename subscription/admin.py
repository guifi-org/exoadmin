from django.contrib import admin

from . import models

admin.site.register(models.Service)

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('identity', 'service', 'active')
    list_filter = ('active', 'service')
