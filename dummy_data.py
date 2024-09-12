
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()

from products.models import   Product ,Brand ,Category 
import random


from faker import Faker

def seed_category(n):
    fake = Faker()
    images = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']

    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,4)]}"
        Category.objects.create(
            name = name ,
            image = image
        )
    print(f'Successfully seeded {n} Category')
        

def seed_brand(n):
    fake = Faker()
    images = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']

    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,4)]}"
        Brand.objects.create(
            name = name ,
            image = image ,
            category = Category.objects.get(id = random.randint(3,22))
        )
    print(f'Successfully seeded {n} Brands')


def seed_products(n):
    fake = Faker()
    images = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
    flag_type = ['New', 'Feature', 'Sale']

    for _ in range(n):
        name = fake.name()
        subtitle = fake.text(max_nb_chars = 500)
        sku = random.randint(1000,100000)
        desc = fake.text(max_nb_chars = 10000)
        price = round(random.uniform(20.99 ,99.99),2)
        image = f"products/{images[random.randint(0,7)]}"
        flag = flag_type[random.randint(0,2)]
        quantity = random.randint(1,100)
        
        
        
        Product.objects.create(
            name = name ,
            subtitle = subtitle ,
            sku = sku ,
            desc = desc,
            price = price,
            image = image ,
            flag = flag,
            quantity = quantity,
            brand = Brand.objects.get(id = random.randint(3,10)),
            category = Category.objects.get(id = random.randint(3,22)),
        )
    print(f'Successfully seeded {n} Product')



seed_category(10)
seed_brand(10)
seed_products(100)