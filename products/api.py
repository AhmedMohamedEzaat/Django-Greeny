from rest_framework.response import Response
from .serializers import ProductSerializer , CategorySerializer , BrandSerializer ,CategoryDetailSerializer,BrandDetailSerializer
from .models import Product , Category , Brand
from rest_framework.decorators import api_view
# import django_filters.rest_framework


### View --->function-----------------------------------------------------------------

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:10]
    data = ProductSerializer(products,many=True).data
    return Response({'Success':True ,'Product List':data})


@api_view(['GET'])
def product_detail(request, id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product).data
    return Response({'Success':True , 'product detail':data})
        
        
        
        
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated





### Generic_View -->classes---------------------------------------------------------------


# class ProductList(generics.ListCreateAPIView):
class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends= [SearchFilter]
    search_fields =['name'] 
    permission_classes=[IsAuthenticated]


# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes=[IsAuthenticated]




class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes=[IsAuthenticated]
    
    
class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes=[IsAuthenticated]
   
   


class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes=[IsAuthenticated]


class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all() 
    permission_classes=[IsAuthenticated]
    
    
    

### ViewSets----->----------------------------------------------------------

from rest_framework import viewsets

class ProductViewSets(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


