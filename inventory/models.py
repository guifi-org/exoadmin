from django.db import models

from django.utils.translation import gettext as _

import datetime

class IP(models.Model):
    ip = models.GenericIPAddressField(
            _('IP address'),
            help_text=_('Can be IPv4 or IPv6'),
         )

    cidr = models.PositiveIntegerField(
            _('CIDR'),
            help_text=_('Put a number if you want more than one IP'),
            null=True,
            blank=True,
         )

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'

    def __str__(self):
        if (self.cidr):
            return "{}/{}".format(self.ip, self.cidr)
        else: 
            return "{}".format(self.ip)

class Item_status(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _('Item status')
        verbose_name_plural = _('Item status')

    def __str__(self):
        return self.name

class Item_type(models.Model):

    name = models.CharField(
        _('Name'),
        max_length=50,
    )

    description = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _('Item type')
        verbose_name_plural = _('Item types')

    def __str__(self):
        return self.name

class Item(models.Model):

    active = models.BooleanField(
        _('Availability'),
        default=True,
        help_text=_(
            'The item is available. If is unavailable it cannot be used anymore and it is there for record purposes'
        ),
    )

    item_status = models.ForeignKey(
        'Item_status',
        verbose_name=_('Item status'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    item_type = models.ForeignKey(
        'Item_type',
        verbose_name=_('Item type'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    name = models.CharField(
        _('Name'),
        max_length=50,
    )

    comments = models.TextField (
        _('Description'),
        max_length=300,
        blank=True,
    )

    acquired = models.DateField(
        _('Acquisition date'),
        default=datetime.date.today,
    )
