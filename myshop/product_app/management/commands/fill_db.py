import json
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from auth_app.models import ShopUser
from product_app.models import Product, ProductCategory

JSON_PATH = 'product_app/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category_id']
            _category = ProductCategory.objects.get(name=category_name)
            product['category_id'] = _category
            new_product = Product(**product)
            new_product.save()

        User.objects.create_superuser('admin', 'admin@django.com', '12345')