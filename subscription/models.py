from django.db import models

from django.utils.translation import gettext as _

import datetime

class Service(models.Model):

    # example of service: membership

    name = models.CharField(
        _("name"),
        max_length=50,
        unique=True
    )

    description = models.TextField(
        _('Description'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

class Subscriber(models.Model):

    active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_(
            'The subscription is active'
        ),
    )

    identity = models.ForeignKey(
        'identity.Identity',
        verbose_name=_("Identity"),
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        verbose_name=_("Service"),
        on_delete=models.CASCADE
    )

    # TODO: check on data entry that start_subs should be greater than end_subs
    # src http://stackoverflow.com/questions/2029295/django-datefield-default-options/2030142#2030142
    start_subs = models.DateField(
        _('Start subscription date'),
        default=datetime.date.today
    )

    # optional date
    # src http://stackoverflow.com/questions/11351619/how-to-make-djangos-datetimefield-optional/11351661#11351661
    end_subs = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        _('Notes'),
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")

    def __str__(self):
        return self.identity.user.username
