from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product ,Brand , Category
from django.db.models import Q  , F , Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Max , Min , Sum , Avg , Count 


def product_list(request):
    products = Product.objects.all()
    # products = Product.objects.aggregate(Count('quantity'))
    # products = Product.objects.filter(price__gt=30)
    # products = Product.objects.filter( Q (name__endswith ="on" ) | ~Q(quantity__gt= 80))
    # products = Product.objects.filter(quantity = F('price'))
    # products = Product.objects.order_by('-name')
    # products = Product.objects.select_related('category').annotate(is_new= Value(True))
    products = Product.objects.select_related('category').annotate(info = Concat('name','flag'))
    
    
    
    return render(request , 'products/product_list_test.html' , {'products':products})


class ProductList(ListView):
    model = Product
    paginate_by = 50
    
class ProductDetail(DetailView):
    model = Product
    
    
class BrandList(ListView):
    model = Brand
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brand_list"] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context
    
    
class BrandDetail(DetailView):
    model = Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    
    
    
class CategoryList(ListView):
    model = Category 