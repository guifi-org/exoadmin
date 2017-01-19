from django.contrib import admin

from . import models

admin.site.register(models.Network_interface_protocol)

@admin.register(models.Network_interface)
class NetinterfaceAdmin(admin.ModelAdmin):
    list_display = ('ip', 'network_interface_protocol')
    # TODO: search IP or identity
