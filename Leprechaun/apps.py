from django.apps import AppConfig


class LeprechaunConfig(AppConfig):
    name = 'Leprechaun'
    def ready(self):
        import Leprechaun.signals
