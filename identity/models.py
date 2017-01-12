from django.db import models

from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Identity(models.Model):

    # src https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(
            User,
            verbose_name=_("User"),
            on_delete=models.CASCADE
    )

    address = models.CharField(
            _("Address"),
            max_length=50
    )

    identity = models.CharField(
            _("ID"),
            help_text=_("Identity Document; the number and/or text that verifies you"),
            max_length=20,
            unique=True,
            primary_key=True,
    )

    place = models.ForeignKey(
            'location.Place',
            verbose_name=_("Place"),
            on_delete=models.CASCADE
    )

    postal_code = models.CharField(
            _("Postal code"),
            max_length=10
    )

    # src https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
    # src http://stackoverflow.com/questions/12725720/django-choices-how-to-set-default-option
    # src https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield
    # src http://stackoverflow.com/questions/4274243/django-print-choices-value
    USER_TYPE = (
            ('I', 'Individual'),
            ('O', 'Organization'),
    )
    user_type = models.CharField(
            _("Type of user"),
            max_length=2,
            choices=USER_TYPE,
            default='I'
    )

    class Meta:
        verbose_name = _("Identity")
        verbose_name_plural = _("Identities")

    def __str__(self):
        return self.user.username