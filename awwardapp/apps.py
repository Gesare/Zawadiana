from django.apps import AppConfig


class AwwardappConfig(AppConfig):
    name = 'awwardapp'
   
   def ready(self):
        import awardapp.signals
