from django.apps import AppConfig


class ExampleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example_app'

    def ready(self):
        from .models.user import User