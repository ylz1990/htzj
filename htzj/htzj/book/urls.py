from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test1),
    # 主页
    path('', views.htzj, name="index"),
    # 添加文章
    # path('add_htzj8888/', views.add, name="add"),
    # path('add_handle/', views.add_handle, name="add_handle"),

    path('case/', views.case, name="case"),
    # 关于公司
    path('about/', views.about, name="about"),
    path('about_1/', views.about_1, name="about_1"),
    path('about_2/', views.about_2, name="about_2"),

    path('contant/', views.contant, name="contant"),
    path('downlist/', views.downlist, name="downlist"),
    path('download/', views.download, name="download"),
    # 文章详情

    path('newlist/<blog_id>', views.newlist, name="newlist"),
    # 文章列表
    path('news/', views.news, name="news"),
    path('news/news_1/', views.news_1, name="news_1"),
    path('news/news_2/', views.news_2, name="news_2"),
    path('news/news_3/', views.news_3, name="news_3"),

    path('products/', views.products, name="products"),
    # 黄金T+D
    path('product_list/', views.product_list, name="product_list"),
    # 纸黄金
    path('gold_college2/', views.gold_college2, name="gold_college2"),
    # COMEX黄金
    path('gold_college3/', views.gold_college3, name="gold_college3"),
    # 伦敦金
    path('gold_college4/', views.gold_college4, name="gold_college4"),
    # 金条
    path('gold_college5/', views.gold_college5, name="gold_college5"),
    # 贵金属
    path('gold_college6/', views.gold_college6, name="gold_college6"),
    # 投资技巧
    path('gold_college7/', views.gold_college7, name="gold_college7"),
    # 黄金投资
    path('gold_college8/', views.gold_college8, name="gold_college8"),
    # 黄金学堂
    path('gold_college9/', views.gold_college9, name="gold_college9"),

    # path('edit/', views.edit, name="edit"),
    # 删除文章
    # path('delete/<blog_id>', views.delete, name="delete"),
    # 修改文章
    # path('alter_htzj8888/<blog_id>', views.alter, name="alter"),
    # 添加用户
    # path('user/', views.user, name="user"),
]