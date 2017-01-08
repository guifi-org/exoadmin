from django.db import models
from django.utils.translation import gettext as _

class State(models.Model):
    name = models.CharField(_("name"), max_length=50)
    code = models.SlugField(_("code"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.name

class Country(models.Model):
    state = models.ForeignKey(State, verbose_name=_("State"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    code = models.SlugField(_("code"), max_length=10, unique=True)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.code

class Province(models.Model):
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    code = models.SlugField(_("code"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Province")
        verbose_name_plural = _("Province")

    def __str__(self):
        return self.name

# in spanish is Población
# src http://forum.wordreference.com/threads/poblaci%C3%B3n-address-form.2762955/
class Region(models.Model):
    province = models.ForeignKey(Province, verbose_name=_("Province"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    code = models.SlugField(_("code"), max_length=10, unique=True)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.code

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
