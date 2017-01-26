from django.db import models

from django.utils.translation import gettext as _

import datetime

class Expense_type(models.Model):

    name = models.CharField (
        _('Name'),
        max_length=50,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _('Expense type')
        verbose_name_plural = _('Expense types')

    def __str__(self):
        return self.name

class Expense(models.Model):

    date = models.DateField(
        ('Date'),
        default=datetime.date.today,
    )

    cost = models.FloatField (
        _('Cost (€)'),
    )

    activity = models.ForeignKey(
        'Activity',
        verbose_name=_('Activity'),
        on_delete=models.CASCADE,
    )

    expense_type = models.ForeignKey (
        'Expense_type',
        verbose_name=_('Expense type'),
        on_delete=models.CASCADE,
        default=1,
    )

    comments = models.CharField (
        _('Comments'),
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __str__(self):
        return self.expense_type.name

class Task(models.Model):

    activity = models.ForeignKey(
        'Activity',
        verbose_name=_('Activity'),
        on_delete=models.CASCADE,
    )

    task = models.CharField (
        _('Task'),
        max_length=50,
    )

    time = models.FloatField (
        _('Time (hours)'),
    )

    identity = models.ForeignKey(
        'identity.Identity',
        verbose_name=_('Identity'),
        on_delete=models.CASCADE,
    )

    date = models.DateField(
        ('Date'),
        default=datetime.date.today,
    )

    comments = models.CharField (
        _('Comments'),
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.task

# types of activities and tasks
class Type(models.Model):

    name = models.CharField (
        _('Name'),
        max_length=50,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _('Activity and task type')
        verbose_name_plural = _('Activity and task types')

    def __str__(self):
        return self.name

class Activity(models.Model):

    accounted = models.BooleanField(
        _('Accounted'),
        default=False,
        help_text=_(
            'This only matters for the type of activity that should be accounted'
        ),
    )

    activity_type = models.ForeignKey(
        'Type',
        verbose_name=_('Activity type'),
        on_delete=models.CASCADE,
        default=1,
    )

    title = models.CharField (
        _('Title'),
        max_length=50,
        unique=True,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    comments = models.TextField (
        _('Comments'),
        max_length=300,
        blank=True,
    )

#    identities = models.ManyToManyField(
#        'identity.Identity',
#        verbose_name = _('Identities'),
#    )


    # TODO this should be autocalculated from inlines entries
    # http://stackoverflow.com/questions/24603874/how-can-i-total-up-the-sum-of-all-prices-in-django-admin
    # non editable?
#    time = models.FloatField (
#        _('Time in hours'),
#        default=0,
#        editable=False,
#    )
#
#    money = models.FloatField (
#        _('Money in €'),
#        default=0
#        editable=False,
#    )


    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.title
