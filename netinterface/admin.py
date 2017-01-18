from django.contrib import admin

from . import models

admin.site.register(models.Network_interface_protocol)
#admin.site.register(models.Network_interface)
@admin.register(models.Network_interface)
class NetinterfaceAdmin(admin.ModelAdmin):
    list_display = ('ip', 'network_interface_protocol', 'get_identity')
    # search IP or identity

    # src http://stackoverflow.com/questions/15306897/django-reverse-lookup-of-foreign-keys
    # src https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward
    def get_identity(self, obj):
        # src https://docs.djangoproject.com/en/dev/topics/db/queries/#retrieving-a-single-object-with-get
        return obj.subscriber_set.all().get().identity
    get_identity.short_description = 'Identity'
