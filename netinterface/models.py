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

    subscriber = models.ForeignKey(
        'subscription.Subscriber',
        verbose_name = _('Subscriber'),
    )

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

    guifi_address = models.GenericIPAddressField(
        _('Guifi 10.x.x.x'),
        help_text=_('This is for IPIP or GRE'),
        null=True,
        blank=True,
    )

    local_address = models.GenericIPAddressField(
        _('Local 192.x.x.x'),
        help_text=_('This is for IPIP or GRE'),
        null=True,
        blank=True,
    )

    remote_address = models.GenericIPAddressField(
        _('Remote 192.x.x.x'),
        help_text=_('This is for IPIP or GRE'),
        null=True,
        blank=True
    )

    # extra parameters for other interface protocols go here

    class Meta:
        verbose_name = _('Network interface')
        verbose_name_plural = _('Network interfaces')

    def __str__(self):
        return "{} {}".format(self.network_interface_protocol, self.ip)
