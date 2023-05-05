import csv
from faker import Faker
from django.utils.text import slugify
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from store.models import Category, Product

# CSV file is location
csv_filepath = '/CSVData/datashortened.csv.csv'

fake_description = Faker()

class Command(BaseCommand):
    help = 'Load data from csv'
    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Category.objects.all().delete()
        Product.objects.all().delete()

        print("table dropped successfully")

        # create table again
        # open the file to read it into th database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/CSVData/datashortened.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create category based on the country of origin
                category, _ = Category.objects.get_or_create(
                    title=row['Country'],
                    slug=slugify(row['Country'])
                )

                # Create a fake description using the Faker library
                description = fake_description.paragraph()

                # adding products into the database
                product = Product.objects.create(
                    category=category,
                    title=row['Description'],
                    slug=slugify(row['title']),
                    description=description,
                    price=row['UnitPrice'],
                    image=None
                )