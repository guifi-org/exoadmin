from django.db import models

from django.utils.translation import gettext as _

class Network_interface_protocol(models.Model):
    name = models.CharField(
            _('name'),
            max_length=20,
            unique=True
    )

    description = models.TextField(
            _('Description'),
            max_length=300,
            blank=True,
    )

    class Meta:
        verbose_name = _('Network interface protocol')
        verbose_name_plural = _('Network interface protocols')

    def __str__(self):
        return self.name

class Network_interface(models.Model):

    ip = models.ForeignKey(
            'netresource.IP',
            verbose_name=_('IP address'),
            on_delete=models.CASCADE
        )

    network_interface_protocol = models.ForeignKey(
            Network_interface_protocol,
            verbose_name=_('Network interface protocol'),
            on_delete=models.CASCADE
        )

    # Why null and blank true? ->
    # http://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django

    local_address = models.GenericIPAddressField(
                        _('Local IP Address'),
                        help_text=_('Can be IPv4 or IPv6'),
                        null=True,
                        blank=True,
                    )

    remote_address = models.GenericIPAddressField(
                        _('Remote IP Address'),
                        help_text=_('Can be IPv4 or IPv6'),
                        null=True,
                        blank=True
                     )

    # extra parameters for other interface protocols go here

    class Meta:
        verbose_name = _('Network interface')
        verbose_name_plural = _('Network interfaces')

    def __str__(self):
        return "{} {}".format(self.network_interface_protocol, self.ip)
