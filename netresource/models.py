from django.db import models

from django.utils.translation import gettext as _

class IP(models.Model):
    ip = models.GenericIPAddressField(
            _('IP address'),
            help_text=_('Can be IPv4 or IPv6'),
         )

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'

    def __str__(self):
        return self.ip
