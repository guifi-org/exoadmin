from django.contrib import admin

from django.utils.translation import gettext as _

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

# src http://stackoverflow.com/questions/3623021/django-exposing-model-method-to-admin/3623025#3623025
# src https://docs.djangoproject.com/en/1.10/ref/contrib/admin/actions/
def update_netiface_counter(self, request, queryset):
    for obj in queryset:
        obj.save()
    self.message_user(request, _('Counters updated'))
update_netiface_counter.short_description = _('Update network interface counter')

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    inlines = (NetinterfaceInline,)
    list_display = ('identity', 'service', 'count_netifaces', 'active',)
    list_filter = ('active', 'service',)
    raw_id_fields = ('identity',)
    actions = (update_netiface_counter,)
