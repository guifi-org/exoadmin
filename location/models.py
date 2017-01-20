from django.db import models
from django.utils.translation import gettext as _

class Municipality(models.Model):

    name = models.CharField(
        _('name'),
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')

    def __str__(self):
        return self.name

# in spanish Población
class Place(models.Model):

    municipality = models.ForeignKey(
        Municipality,
        verbose_name=_('Municipality'),
        on_delete=models.CASCADE
    )

    name = models.CharField(
        _('name'),
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def __str__(self):
        return '{}, {}'.format(self.name, self.municipality)
