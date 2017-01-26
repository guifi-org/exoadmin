from django.contrib import admin

from . import models

@admin.register(models.Expense_type)
class Expense_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(models.Expense)
class Expense(admin.ModelAdmin):
    list_display = ('activity', 'expense_type', 'cost', 'comments', 'date',)

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('activity', 'task_type', 'identity', 'time', 'comments', 'date',)

class ExpenseInline(admin.TabularInline):
    model = models.Expense
    extra = 0

class TaskInline(admin.TabularInline):
    model = models.Task
    extra = 0
    raw_id_fields = ('identity',)

@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = (TaskInline, ExpenseInline,)
    readonly_fields = ('time_report','money_report',)
    list_display = ('title', 'activity_type', 'time_report', 'money_report')
    search_fields = ('title',)

    def time_report(self, instance):
        # src http://stackoverflow.com/questions/24603874/how-can-i-total-up-the-sum-of-all-prices-in-django-admin
        # src https://docs.djangoproject.com/en/1.10/ref/models/querysets/#values-list
        return sum(models.Task.objects.filter(activity__id = instance.id).values_list('time', flat=True))
    time_report.short_description = 'Spend time (hours)'

    def money_report(self, instance):
        return sum(models.Expense.objects.filter(activity__id = instance.id).values_list('cost', flat=True))
    money_report.short_description = 'Expenses (€)'
