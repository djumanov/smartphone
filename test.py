
import requests

base_url = 'http://127.0.0.1:8000/'

def get_all_products():
    r = requests.get(url=base_url+'products/')
    print(r.json())

def add_product(product):
    r = requests.post(url=base_url+'add_product/', data=product)

    print(r.json())

json_product = {}
json_product['name']       = 'A02'
json_product['company']    = 'Samsung'
json_product['color']      = 'black'
json_product['RAM']        = '4GB'
json_product['memory']     = '32GB'
json_product['price']      = 120.0
json_product['img_url']    = 'https://www.creditasia.uz/upload/iblock/9cb/smartfon-samsung-galaxy-a02-sm-a022g-ds-32gb-red-1.jpg'

# add_product(json_product)
get_all_products()