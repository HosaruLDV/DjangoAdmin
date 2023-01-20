from django.core.management import BaseCommand

from hsr.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category = [
            {'name':'Мясо', 'description':'12'},
            {'name':'Молоко', 'description':'13'},
            {'name':'Яйца', 'description':'14'},
            {'name':'Гвозди', 'description':'15'}

        ]

        category_list = []
        for item in category:
            category_list.append(**item)

        Category.objects.bulk_create(category_list)


