from django.db import models

from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Identified(models.Model):

    # src https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)

    address = models.CharField(_("Address"), max_length=50)

    # approximation; fix it to be more precise
    identity = models.CharField(_("Identity"), max_length=9, unique=True)

    place = models.ForeignKey('location.Place', verbose_name=_("Place"), on_delete=models.CASCADE)

    postal_code = models.CharField(_("Postal code"), max_length=10)

    # src https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
    # src http://stackoverflow.com/questions/12725720/django-choices-how-to-set-default-option
    # src https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield
    # src http://stackoverflow.com/questions/4274243/django-print-choices-value
    USER_TYPE = (
            ('I', 'Individual'),
            ('O', 'Organization'),
    )
    user_type = models.CharField(_("Type of user"), max_length=2, choices=USER_TYPE, default='I')

    class Meta:
        verbose_name = _("Identified")
        verbose_name_plural = _("Identified")

    def __str__(self):
        return self.user.username
