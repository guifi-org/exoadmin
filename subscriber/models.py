from django.db import models

from django.utils.translation import gettext as _

import datetime

class Subscriber(models.Model):

    active_subs = models.BooleanField(
        _('Active subscription'),
        default=True,
        help_text=_(
            'The subscription is active; redundant, but useful to do a quick filter'
        ),
    )

    identified = models.OneToOneField(
        'identified.Identified',
        verbose_name=_("Identified user"),
        on_delete=models.CASCADE
    )

    org_member = models.BooleanField(
        _('Organization Member'),
        default=True,
        help_text=_(
            'True if this user becomes member/partner with this '
            'subscription of the organization. False if is just a client'
        ),
    )

    # Dates as a list

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
    
    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")

    def __str__(self):
        return self.identified.user.username
