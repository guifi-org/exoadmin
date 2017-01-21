from django.contrib import admin

from . import models

# inline from another app inspired from:
# src http://stackoverflow.com/questions/32590901/how-can-i-add-inlines-to-the-modeladmin-of-another-app-without-a-circular-depen/32590902#32590902
from netinterface.models import Network_interface

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class NetinterfaceInline(admin.StackedInline):
    model = Network_interface
    extra = 0

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    inlines = (NetinterfaceInline,)
    list_display = ('identity', 'service', 'active', 'end_date')
    list_filter = ('active', 'service')
