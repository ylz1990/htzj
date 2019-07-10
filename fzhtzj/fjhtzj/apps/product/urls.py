from django.urls import path
from . import views

# 大咖论道
app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product_info/', views.ProductInfoView.as_view(), name='product_info'),
    path('product_info2/', views.ProductInfo2View.as_view(), name='product_info2'),
    path('product_info3/', views.ProductInfo3View.as_view(), name='product_info3'),
    path('product_info4/', views.ProductInfo4View.as_view(), name='product_info4'),
    path('product_info5/', views.ProductInfo5View.as_view(), name='product_info5'),
    path('product_info6/', views.ProductInfo6View.as_view(), name='product_info6'),
    path('product_info7/', views.ProductInfo7View.as_view(), name='product_info7'),
    path('product_info8/', views.ProductInfo8View.as_view(), name='product_info8'),
]