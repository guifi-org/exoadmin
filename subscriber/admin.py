from django.contrib import admin

from . import models

#admin.site.register(models.Subscriber)

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('identified', 'active_subs', 'service')
    list_filter = ('active_subs', 'service')
#    list_display = ('identified', 'active_subs', 'org_member')
#    list_filter = ('active_subs', 'org_member')

admin.site.register(models.Service)
