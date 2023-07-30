from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from os import getenv


class Command(BaseCommand):
    help = "Create SuperUser"

    def handle(self, *args, **options):
        username = getenv('DJANGO_SUPERUSER_USERNAME')
        password = getenv('DJANGO_SUPERUSER_PASSWORD')

        user = get_user_model().objects.filter(username=username).first()
        if not user:
            get_user_model().objects.create_superuser(username=username, password=password, email='')
