from django.urls import path
from . import views

# 关于公司
app_name = 'about'

urlpatterns = [
    path("", views.AboutView.as_view(), name='company'),
    path("company_2", views.About2View.as_view(), name='company_2'),
    path("company_3", views.About3View.as_view(), name='company_3'),
]