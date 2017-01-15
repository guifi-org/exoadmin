from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class NetinterfaceConfig(AppConfig):
    name = 'netinterface'
    verbose_name = _('Network interface')
