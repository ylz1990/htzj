from django.shortcuts import render
from django.views import View
# Create your views here.



class AboutView(View):
    """
    显示关于公司
    """
    def get(self,request):
        return render(request, "about/about.html")


class About2View(View):
    """
    显示企业文化
    """
    def get(self,request):
        return render(request, "about/about_2.html")

class About3View(View):
    """
    显示经营理念
    """
    def get(self,request):
        return render(request, "about/about_3.html")