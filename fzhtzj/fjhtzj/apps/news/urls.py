from django.urls import path
from . import views

# 新闻资讯
app_name = 'news'

urlpatterns = [
    path('', views.NewListView.as_view(), name='new_list'),
    path('new_list2/', views.NewList2View.as_view(), name='new_list2'),
    path('new_list3/', views.NewList3View.as_view(), name='new_list3'),
    path('new_info/<int:new_id>', views.NewInfoView.as_view(), name='new_info'),
]