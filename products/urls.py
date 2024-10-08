from django.urls import path , include
from .views import ProductList , ProductDetail , BrandList , BrandDetail , CategoryList ,product_list
from .api import  BrandDetailAPI,BrandListAPI,CategoryDetailAPI,CategoryListAPI,ProductDetailAPI,ProductListAPI , ProductViewSets
# product_list_api , product_detail ,

from rest_framework import routers

router = routers.DefaultRouter()
router.register('myproducts',ProductViewSets)
 
 

app_name = 'Product'

urlpatterns = [
    
    path('testing/', product_list),
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>' , ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>' , BrandDetail.as_view(), name='brand_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),
    
    
    
    # path('api/list', product_list_api),
    # path('api/list/<int:id>', product_detail),
    
    
    path('api/list/cbv/',ProductListAPI.as_view()),
    path('api/list/cbv/<int:pk>',ProductDetailAPI.as_view()),
    path('api/category',CategoryListAPI.as_view()),
    path('api/category/<int:pk>', CategoryDetailAPI.as_view()),
    path('api/brand',BrandListAPI.as_view()),
    path('api/brand/<int:pk>', BrandDetailAPI.as_view()),

    path('myapi/',include(router.urls))

]

 