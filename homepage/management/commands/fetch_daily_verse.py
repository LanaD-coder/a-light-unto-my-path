from django.core.management.base import BaseCommand
from homepage.views import fetch_daily_verse


class Command(BaseCommand):
    help = "Fetches and stores the daily Bible verse"

    def handle(self, *args, **kwargs):
        fetch_daily_verse()
        self.stdout.write
        (self.style.SUCCESS
         ("Successfully fetched and stored the daily verse."))
