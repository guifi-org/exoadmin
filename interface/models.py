from django.db import models

from django.utils.translation import gettext as _

class Interface_protocol(models.Model):
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
        verbose_name = _('Interface protocol')
        verbose_name_plural = _('Interface protocols')

    def __str__(self):
        return self.name

class Interface(models.Model):

    ip = models.ForeignKey(
            'netresource.IP',
            verbose_name=_('IP'),
            on_delete=models.CASCADE
        )

    interface_protocol = models.ForeignKey(
            Interface_protocol,
            verbose_name=_('Interface protocol'),
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
        verbose_name = _('Interface')
        verbose_name_plural = _('Interfaces')

    def __str__(self):
        return "{} {}".format(self.interface_protocol, self.ip)
