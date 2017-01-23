from django.db import models

from django.utils.translation import gettext as _

from django.core.exceptions import ValidationError

from inventory.models import IP

import ipaddress

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

    # ip assignment must be unique
    ip = models.GenericIPAddressField(
        _('IP address'),
#        help_text=_('Assigned IP address to subscription'),
        unique = True,
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

    # check ip address (see ValidationError)
    # [validation] src https://docs.djangoproject.com/en/1.10/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
    def clean(self):
        verified = False
        # [evaluation] src https://docs.djangoproject.com/en/1.10/ref/models/querysets/#when-querysets-are-evaluated
        for inventory_ip in IP.objects.all():
            # [check ip in network] src http://stackoverflow.com/questions/819355/how-can-i-check-if-an-ip-is-in-a-network-in-python/1004527#1004527
            # [no strict check] src https://docs.python.org/3/howto/ipaddress.html#defining-networks
            if ipaddress.ip_address(self.ip) in ipaddress.ip_network(inventory_ip, strict=False):
                verified = True
                break
        # src http://stackoverflow.com/questions/6117733/negation-in-python/6117762#6117762
        if not verified:
            # src http://stackoverflow.com/questions/6333738/django-how-to-specify-which-field-a-validation-fails-on/6347281#6347281
            raise ValidationError({'ip': [_('IP does not belong to any existing Network or IP in Inventory')]})
