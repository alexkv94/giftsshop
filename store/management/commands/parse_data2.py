import csv
from faker import Faker
from django.utils.text import slugify
from pathlib import Path
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from store.models import Category, Product
from decimal import Decimal, InvalidOperation


fake_description = Faker()

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Category.objects.all().delete()
        print("Category table dropped successfully")

        Product.objects.all().delete()
        print("table dropped successfully")

        # create table again
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/store/CSVData/datashortened.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')

            n = 0
            m = 0
            next(reader) #skip header

            categories = set()
            for row in reader:
                categories.add(row[7])

                n+=1
                print(f'{n} iterations completed in first loop')


            for unique_category in categories:
                if unique_category:

                    category = Category.objects.create(
                        title=unique_category,
                        slug = slugify(unique_category)

                    )
                    category.save()
            print('completed insertion to "category table"')

            f.seek(0)
            next(reader)  # skip header
            for row in reader:
                product_description = fake_description.paragraph()

                try:
                    price = Decimal(row['UnitPrice'])
                except InvalidOperation:
                    price = Decimal('0.0')

                if row[7]:

                    product = Product.objects.create(
                        category=row[7],
                        title=row[2],
                        slug=slugify(row[2]),
                        description=product_description,
                        price=price,
                        image=None
                    )
                product.save()

            m += 1
            print(f'{m} iterations completed for second table')





