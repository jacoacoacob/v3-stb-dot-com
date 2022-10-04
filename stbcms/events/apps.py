from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self) -> None:
        from .signal_handlers import register_signal_handlers
        register_signal_handlers()
        