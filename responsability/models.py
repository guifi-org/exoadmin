from django.db import models

from django.utils.translation import gettext as _

import datetime

# role (president, treasurer), projects, equipment, tasks
class Type_of_responsability(models.Model):

    name = models.CharField (
        _('Name'),
        max_length=20,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _('Type of responsability')
        verbose_name_plural = _('Type of responsabilities')

    def __str__(self):
        return self.name

class Responsability(models.Model):

    active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_(
            'The responsability is active'
        ),
    )

    type_of_responsability = models.ForeignKey(
        'Type_of_responsability',
        verbose_name=_('Type of responsability'),
        on_delete=models.CASCADE,
    )

    title = models.CharField (
        _('Title'),
        max_length=20,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    notes = models.TextField (
        _('Notes'),
        max_length=300,
        blank=True,
    )

    identities = models.ManyToManyField(
        'identity.Identity',
        verbose_name = _('Identities'),
    )

    start_date = models.DateField(
        _('Start responsability date'),
        default=datetime.date.today,
    )
    
    end_date = models.DateField(
        _('End responsability date'),
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = _('Responsability')
        verbose_name_plural = _('Responsabilities')

    def __str__(self):
        return self.title
