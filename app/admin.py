from django.contrib import admin
from .models import Product

db_tables = [Product]

admin.site.register(model_or_iterable=db_tables)
