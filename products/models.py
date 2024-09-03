from django.db import models
from django.utils.translation import gettext as _

FLAG_OPTION=(
    ("festure","festure"),
    ("sale","sale"),
    ("new","new"),
)


class Products(models.Model):
    name = models.CharField(max_length=100 , verbose_name=_("Name"))
    subtitle = models.CharField(_("Subtitle"),max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description"), max_length=10000)
    price = models.FloatField(_("Price"))
    flag = models.CharField(_("Flag"),max_length=10 ,choices=FLAG_OPTION)
    quanitity = models.IntegerField(_("Quanitity"))
    
    

class Products_Images(models.Model):
    pass


class Brand(models.Model):
    pass



class Category(models.Model):
    pass


class ProdactReview(models.Model):
    pass
