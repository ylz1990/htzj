from django.urls import path
from . import views

app_name = 'htzj'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('about/', views.AboutView.as_view(), name='about'),
    # path('case_info/', views.CaseInfoView.as_view(), name='case_info'),
    # path('case_list/', views.CaseListView.as_view(), name='case_list'),
    # path('new_list/', views.NewListView.as_view(), name='new_list'),
    # path('new_info/', views.NewInfoView.as_view(), name='new_info'),
    # path('product_info/', views.ProductInfoView.as_view(), name='product_info'),
    # path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    # path('news_list/', views.NewsListView.as_view(), name='news_list'),
    # path('news_info/', views.NewsInfoView.as_view(), name='news_info'),
]
