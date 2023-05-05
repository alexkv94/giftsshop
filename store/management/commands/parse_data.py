import csv
from faker import Faker
from django.utils.text import slugify
from pathlib import Path
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from store.models import Category, Product
from decimal import Decimal, InvalidOperation


# CSV file location
csv_filepath = 'store/CSVData/datashortened.csv.csv'

fake_description = Faker()

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Category.objects.all().delete()
        Product.objects.all().delete()

        print("table dropped successfully")

        # create table again
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/store/CSVData/datashortened.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create category based on the country of origin
                category, created = Category.objects.get_or_create(
                    title=row['Country'],
                    slug=slugify(row['Country'])
                )

                # Create a fake description using the Faker library
                description = fake_description.paragraph()

                # Convert price to a decimal
                try:
                    price = Decimal(row['UnitPrice'])
                except InvalidOperation:
                    price = Decimal('0.0')

                # adding products into the database
                try:
                    product = Product.objects.create(
                        category=category,
                        title=row['Description'],
                        slug=slugify(row['Description']),
                        description=description,
                        price=price,
                        image=None
                    )
                except ValidationError as e:
                    print(f"Error creating product {row['Description']}: {e.message_dict}")
            print('added data to tables')
