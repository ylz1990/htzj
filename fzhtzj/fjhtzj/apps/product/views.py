from django.shortcuts import render
from django.views import View
# Create your views here.


class ProductListView(View):
    """
    显示大咖论道
    """
    def get(self,request):
        return render(request, "product/product_list.html")

class ProductInfoView(View):
    """
    显示机构精评详情
    """
    def get(self,request):
        return render(request, "product/product_info.html")


class ProductInfo2View(View):
    """
    显示机构观点详情
    """
    def get(self,request):
        return render(request, "product/product_info2.html")

class ProductInfo3View(View):
    """
    显示名家策略详情
    """
    def get(self,request):
        return render(request, "product/product_info3.html")


class ProductInfo4View(View):
    """
    显示名家精评详情
    """
    def get(self,request):
        return render(request, "product/product_info4.html")

class ProductInfo5View(View):
    """
    显示财富管理详情
    """
    def get(self,request):
        return render(request, "product/product_info5.html")

class ProductInfo6View(View):
    """
    显示财富管理详情
    """
    def get(self,request):
        return render(request, "product/product_info6.html")

class ProductInfo7View(View):
    """
    显示财富管理详情
    """
    def get(self,request):
        return render(request, "product/product_info7.html")

class ProductInfo8View(View):
    """
    显示财富管理详情
    """
    def get(self,request):
        return render(request, "product/product_info8.html")