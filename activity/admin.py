from django.contrib import admin

from . import models
#from .models import Task
#from .models import Material
#from activity.models import *
#from activity.models import Task
#from activity.models import Material

admin.site.register(models.Material)
admin.site.register(models.Task)

class MaterialInline(admin.TabularInline):
    model = models.Material
    extra = 0

class TaskInline(admin.TabularInline):
    model = models.Task
    extra = 0
    raw_id_fields = ('identity',)

@admin.register(models.Activity_type)
class Activity_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
#    filter_horizontal = ('identities',)
    inlines = (TaskInline, MaterialInline,)
    readonly_fields = ('time_report','money_report',)

    def time_report(self, instance):
        # src http://stackoverflow.com/questions/24603874/how-can-i-total-up-the-sum-of-all-prices-in-django-admin
        # src https://docs.djangoproject.com/en/1.10/ref/models/querysets/#values-list
        return sum(models.Task.objects.values_list('time', flat=True))
    time_report.short_description = 'Time'

    def money_report(self, instance):
        return sum(models.Material.objects.values_list('cost', flat=True))
    money_report.short_description = 'Money'

