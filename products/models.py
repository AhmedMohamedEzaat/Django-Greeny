from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.aggregates import Avg 



FLAG_OPTION=(
    ("feature","feature"),
    ("sale","sale"),
    ("new","new"),
)


class Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name=_("Name"))
    subtitle = models.CharField(_("Subtitle"),max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description"), max_length=10000)
    price = models.FloatField(_("Price"))
    image = models.ImageField(upload_to='products/')
    flag = models.CharField(_("Flag"),max_length=10 ,choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))
    brand =models.ForeignKey('Brand', related_name='product_brand' ,on_delete=models.SET_NULL,null=True,blank=True)
    category =models.ForeignKey('Category', related_name='product_category' ,on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True , blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Product, self).save(*args, **kwargs) # Call the real save() method
    
    
    def avg_review(self):
        avg = self.product_review.aggregate(avg = Avg('rate') )
        return avg
    
    
class ProductsImages(models.Model):
    product = models.ForeignKey(Product , related_name='product_image', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return str(self.product)
    
    
    
    
    
class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to="brands/"  ,null=True,  blank=True)
    category =models.ForeignKey('Category', related_name='brand_Category' ,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name





class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to="category/"  ,null=True,  blank=True)

    def __str__(self):
        return self.name





class ProductReview(models.Model):
    user = models.ForeignKey(User ,related_name='user_review',verbose_name=_("Name") ,on_delete=models.CASCADE )
    product = models.ForeignKey(Product,related_name='product_review',verbose_name=_("Product"),on_delete=models.CASCADE)
    rate =models.IntegerField(_("Rate") ,validators=[MinValueValidator(0 ), MaxValueValidator(5)])
    review = models.TextField(_("Review"),max_length=500)
    created_at = models.DateTimeField(_("Create_at"),default=timezone.now)
    
    def __str__(self):
        return str(self.user)