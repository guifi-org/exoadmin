from django.contrib import admin

from . import models

@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'state')

@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country')
    list_filter = ('country', 'country__state')
    prepopulated_fields = {'code': ('name',)}

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'province')
    list_filter = ('province', 'province__country', 'province__country__state')
    prepopulated_fields = {'code': ('name',)}

#@admin.register(models.Address)
#class AddressAdmin(admin.ModelAdmin):
#    list_display = ('address', 'postal_code', 'region')
#    list_filter = ('city', 'city__state', 'city__state__country')
