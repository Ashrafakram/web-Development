from typing import Any
from bloging.models import Category
from django.core.management.base import BaseCommand
#import random


class Command(BaseCommand):
    help = "This command inserts categories data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Category.objects.all().delete()

        categories = ['Sports', 'Technologies', 'Nature', 'Art', 'Food']

        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("completed inserting Data:)"))

