import csv
from faker import Faker
from django.utils.text import slugify
from myapp.models import Category, Product

# CSV file is location
csv_filepath = 'data.csv'

fake_description = Faker()

with open(csv_filepath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Create category based on the country of origin
        category, _ = Category.objects.get_or_create(
            title=row['countryOfOrigin'],
            slug=slugify(row['countryOfOrigin'])
        )

        # Create a fake description using the Faker library
        description = fake_description.paragraph()

        # adding products into the database
        product = Product.objects.create(
            category=category,
            title=row['title'],
            slug=slugify(row['title']),
            description=description,
            price=row['unitPrice'],
            image=None
        )