
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()

from products.models import   Product ,Brand ,Category 
import random


from faker import Faker

def seed_category(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg','31.jpg','32.jpg','33.jpg','34.jpg','35.jpg','36.jpg']

    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,35)]}"
        Category.objects.create(
            name = name ,
            image = image
        )
    print(f'Successfully seeded {n} Category')
        

def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg','31.jpg','32.jpg','33.jpg','34.jpg','35.jpg','36.jpg']

    for _ in range(n):
        name = fake.name()
        image = f"brands/{images[random.randint(0,34)]}"
        # image = f"brands/{images.objects.all().order_by('?')[0]}"
        Brand.objects.create(
            name = name ,
            image = image ,
            # category = Category.objects.get(id = random.randint(114,123)),
            category = Category.objects.all().order_by('?')[0],
        )
    print(f'Successfully seeded {n} Brands')


def seed_products(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg','31.jpg','32.jpg','33.jpg','34.jpg','35.jpg','36.jpg']
    # images = f'product/images/{random.randint(0,17)}.jbg'

    flag_type = ['New', 'Feature', 'Sale']

    for _ in range(n):
        name = fake.name()
        subtitle = fake.text(max_nb_chars = 500)
        sku = random.randint(1000,100000)
        desc = fake.text(max_nb_chars = 10000)
        price = round(random.uniform(20.99 ,99.99),2)
        # image = f"product/{images[random.randint(0,35)]}"
        image = f"product/{images[random.randint(0,34)]}"
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
            # brand = Brand.objects.get(id = random.randint(59,60)),
            brand = Brand.objects.all().order_by('?')[0],
            category = Category.objects.all().order_by('?')[0],
            # category = Category.objects.get(id = random.randint(114,123)),
        )
    print(f'Successfully seeded {n} Product')



# seed_category(25)
# seed_brand(30)
# seed_products(1000)