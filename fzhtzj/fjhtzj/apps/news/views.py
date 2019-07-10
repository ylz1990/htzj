from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from news import models
from django.conf import settings
# Create your views here.


class NewInfoView(View):
    """
    显示新闻详情页
    """
    def get(self,request,new_id):
        new = models.News.objects.get(id=new_id)
        # 上一篇
        previoud_new = models.News.objects.filter(id__gt=new.id).last()
        # 下一篇
        next_new = models.News.objects.filter(id__lt=new.id).first()
        return render(request, "news/new_info.html",locals())

class NewListView(View):
    """
    显示新闻列表页
    """
    def get(self,request):
        news_all_list = models.News.objects.only('id', 'title',"create_date").filter(tags__contains="公司新闻")
        paginator = Paginator(news_all_list, settings.EACH_PAGE_NUM)   #  每10篇进行分页
        page_num = request.GET.get('page', 1)   #  获取URL 传进来的页码数
        page_of_news = paginator.get_page(page_num)  # 获取每页的新闻数
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number # 获取当前页码
        # page_range = [currentr_page_num-2,currentr_page_num-1,currentr_page_num,currentr_page_num+1,currentr_page_num+2]
        # 获取当前页码的前两页和后两页
        page_range = [ x for x in range(int(currentr_page_num)- 2,int(currentr_page_num)+ 3) if 0 < x <= paginator.num_pages]
        return render(request, "news/new_list.html", locals())


# http://www.dlqh.com/page-1-1.php
class NewList2View(View):
    """
    显示新闻列表页
    """
    def get(self,request):
        news_all_list = models.News.objects.only('id', 'title',"create_date").filter(tags__contains="行业资讯")
        paginator = Paginator(news_all_list, settings.EACH_PAGE_NUM)
        page_num = request.GET.get("page", 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if 0 < x <= paginator.num_pages]
        return render(request, "news/new_list_2.html", locals())

# http://www.dyhjw.com/gold/yhdt.html
class NewList3View(View):
    """
    显示新闻列表页
    """
    def get(self,request):
        news_all_list = models.News.objects.only('id', 'title',"create_date").filter(tags__contains="市场动态")
        paginator = Paginator(news_all_list, settings.EACH_PAGE_NUM)
        page_num = request.GET.get("page", 1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        currentr_page_num = page_of_news.number
        page_range = [x for x in range(int(currentr_page_num) - 2, int(currentr_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "news/new_list_3.html", locals())