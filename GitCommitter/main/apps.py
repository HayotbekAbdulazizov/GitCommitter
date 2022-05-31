from django.apps import AppConfig

from jobs import updater

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
    	updater.start()