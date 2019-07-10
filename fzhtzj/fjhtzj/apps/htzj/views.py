from django.shortcuts import render
from django.views import View
from news.models import News
from college.models import RealTimeNews
# Create your views here.



class IndexView(View):
    """
    显示主页
    """
    def get(self, request):
        news = News.objects.filter()[0:6]
        realnews = RealTimeNews.objects.filter()[0:5]
        return render(request, "htzj/index.html",locals())



class ContactView(View):
    """
    显示联系我们
    """
    def get(self,request):
        return render(request, "htzj/contact.html")

