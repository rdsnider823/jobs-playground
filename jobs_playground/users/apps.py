from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "jobs_playground.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import jobs_playground.users.signals  # noqa: F401
        except ImportError:
            pass
