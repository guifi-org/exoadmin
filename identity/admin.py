from django.contrib import admin

from . import models

from django.contrib.auth.models import User

@admin.register(models.Payment_method)
class Payment_method_Admin(admin.ModelAdmin):
    list_display = ('payment_method' , 'description',)

@admin.register(models.Identity)
class IdentifiedAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'user_type')
    list_filter = ('user_type',)
    raw_id_fields = ('user',)

    # src http://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First name'
    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last name'
