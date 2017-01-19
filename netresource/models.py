from django.db import models

from django.utils.translation import gettext as _

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
