from django.db import models

from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Payment_method(models.Model):

    payment_method = models.CharField(
        _('Payment method'),
        max_length=50
    )

    class Meta:
        verbose_name = _('Payment method')
        verbose_name_plural = _('Payment methods')

    def __str__(self):
        return self.payment_method

class Identity(models.Model):

    # src https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )

    address = models.CharField(
        _('Address'),
        max_length=50
    )

    # in spain this is NIF for individual and CIF for organization
    identity = models.CharField(
        _('ID'),
        help_text=_('Identity Document; the number and/or text that verifies you'),
        max_length=20,
        unique=True,
    )

    place = models.ForeignKey(
        'location.Place',
        verbose_name=_('Place'),
        on_delete=models.CASCADE
    )

    postal_code = models.CharField(
        _('Postal code'),
        max_length=10
    )

    # how to do choices
    # src https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
    # src http://stackoverflow.com/questions/12725720/django-choices-how-to-set-default-option
    # src https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield
    # src http://stackoverflow.com/questions/4274243/django-print-choices-value
    # how to prepare choices for translation
    # src http://stackoverflow.com/questions/16088849/how-to-translate-dynamic-form-choices/16088999#16088999
    USER_TYPE = (
        ('Individual', _('Individual')),
        ('Organization', _('Organization')),
    )
    user_type = models.CharField(
         _('Type of user'),
         max_length=20,
         choices=USER_TYPE,
         default='Individual'
    )

    payment_method = models.ForeignKey(
        'Payment_method',
        verbose_name=_('Payment method'),
        on_delete=models.CASCADE,
        default=1,
    )

    # TODO check https://en.wikipedia.org/wiki/International_Bank_Account_Number#Structure
    iban = models.CharField(
        ('IBAN'),
        max_length=32,
        blank=True,
        help_text=_('International Bank Account Number')
    )

    class Meta:
        verbose_name = _('Identity')
        verbose_name_plural = _('Identities')

    def __str__(self):
        return "{} ({} {})".format(self.user.username, self.user.first_name, self.user.last_name)
