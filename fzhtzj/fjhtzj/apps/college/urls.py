from django.urls import path
from . import views

# 黄金学院
app_name = 'college'

urlpatterns = [
    path("", views.CaseListView.as_view(), name='case_list'),
    path("college2/", views.CaseList2View.as_view(), name='case_list2'),
    path("college3/", views.CaseList3View.as_view(), name='case_list3'),
    path("college4/", views.CaseList4View.as_view(), name='case_list4'),
    path("case_info/<int:new_id>", views.CaseInfoView.as_view(), name='case_info'),
]