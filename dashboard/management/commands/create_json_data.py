import json
from django.core.management.base import BaseCommand
from dashboard.models import JsonData  # Import the appropriate model

class Command(BaseCommand):
    help = 'Upload JSON data to PostgreSQL'

    def handle(self, *args, **options):
        json_file_path = 'dashboard/data/jsondata.json'  # Adjust the path to your JSON file

        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        for item in json_data:
            JsonData.objects.create(data=item)

        self.stdout.write(self.style.SUCCESS('JSON data uploaded successfully'))
