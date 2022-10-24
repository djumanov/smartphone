from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Product


def convert_to_json(product: Product) -> dict:
    json_product = {}

    json_product['id']         = product.id
    json_product['name']       = product.name
    json_product['company']    = product.company
    json_product['color']      = product.color
    json_product['RAM']        = product.RAM
    json_product['memory']     = product.memory
    json_product['price']      = product.price
    json_product['created_at'] = product.created_at
    json_product['updated_at'] = product.updated_at
    json_product['img_url']    = product.img_url

    return json_product

def get_products(request: HttpRequest):
    if request.method == 'GET':
        products = Product.objects.all()
        json_products = {'products': []}
        if products:
            for product in products:
                json_products['products'].append(convert_to_json(product))
        else:
            json_products['products'] = []
        
        return JsonResponse(json_products)

def get_product_by_id(request: HttpRequest):
    pass

def get_companies(request: HttpRequest):
    pass

def get_products_by_company(request: HttpRequest):
    pass

def get_products_by_name(request: HttpRequest):
    pass

def get_products_by_color(request: HttpRequest):
    pass

def get_products_by_price(request: HttpRequest):
    pass

def get_products_by_ram(request: HttpRequest):
    pass

def add_product(request: HttpRequest):
    pass

def add_products(request: HttpRequest):
    pass

def update_product_by_id(request: HttpRequest):
    pass

def update_products_by_ids(request: HttpRequest):
    pass

def delete_product_by_id(request: HttpRequest):
    pass

def delete_products_by_ids(request: HttpRequest):
    pass

