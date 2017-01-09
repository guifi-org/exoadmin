from django.db import models
from django.utils.translation import gettext as _

class Municipality(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Municipality")
        verbose_name_plural = _("Municipality")

    def __str__(self):
        return self.name

# in spanish Población
class Place(models.Model):
    municipality = models.ForeignKey(Municipality, verbose_name=_("Municipality"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")

    def __str__(self):
        return self.name

#class Address(models.Model):
#    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.CASCADE)
#    address = models.CharField(_("address"), max_length=100)
#    postal_code = models.CharField(_("postal code"), max_length=10)
## FIXME
##    person = models.ForeignKey('accounting.Person', verbose_name=_("person"), blank=True, null=True, related_name='+', on_delete=models.CASCADE)
#
#    class Meta:
#        verbose_name = _("Address")
#        verbose_name_plural = _("Addresses")
#
#    def __str__(self):
#        return "{} {} {}".format(self.address, self.postal_code, self.city.name)
