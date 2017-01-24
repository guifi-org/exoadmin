from django.db import models

from django.utils.translation import gettext as _

import datetime

# talk, workshop, installation, deployment
class Activity_type(models.Model):

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
        verbose_name = _('Activity type')
        verbose_name_plural = _('Activity types')

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
        'Activity_type',
        verbose_name=_('Activity type'),
        on_delete=models.CASCADE,
    )

    title = models.CharField (
        _('Title'),
        max_length=50,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    identities = models.ManyToManyField(
        'identity.Identity',
        verbose_name = _('Identities'),
    )

    time = models.FloatField (
        _('Time in hours'),
        blank=True,
    )

    time_notes = models.TextField (
        _('Time description'),
        max_length=300,
        blank=True,
    )

    money = models.FloatField (
        _('Money in €'),
        blank=True,
        null=True,
    )

    money_notes = models.TextField (
        _('Money description'),
        max_length=300,
        blank=True,
    )

    start_date = models.DateField(
        ('Start activity'),
        default=datetime.date.today,
    )

    end_date = models.DateField(
        ('End activity'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.title
