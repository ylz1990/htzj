from django.shortcuts import render
from django.views import View
from college import models
from django.core.paginator import Paginator
from news.models import News
# Create your views here.


class CaseInfoView(View):
    """
    显示投资学院新闻详情
    """
    def get(self,request,new_id):
        new = models.RealTimeNews.objects.get(id = new_id)
        # 上一篇
        previoud_new = models.RealTimeNews.objects.filter(id__gt=new.id).last()
        # 下一篇
        next_new = models.RealTimeNews.objects.filter(id__lt=new.id).first()
        return render(request, "college/case_info.html",locals())


# http://www.dyhjw.com/gold/nyhj.html
class CaseListView(View):
    """
    显示投资学院-实时快讯
    """
    def get(self,request):
        # 显示新闻的文章
        news_all = News.objects.only('id', 'title',"create_date").filter()[0:9]

        news_all_list = models.RealTimeNews.objects.only('id', 'title','image_url').filter()
        paginator = Paginator(news_all_list,12)
        page_num = request.GET.get("page",1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        current_page_num = page_of_news.number
        page_range = [x for x in range(int(current_page_num) - 2, int(current_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "college/case_list.html", locals())

class CaseList2View(View):
    """
    显示投资学院-专家点评
    """
    def get(self,request):
        news_all = News.objects.only('id', 'title', "create_date").filter()[0:9]
        news_all_list = models.ExpertComments.objects.only('id', 'title','image_url').filter()
        paginator = Paginator(news_all_list,12)
        page_num = request.GET.get("page",1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        current_page_num = page_of_news.number
        page_range = [x for x in range(int(current_page_num) - 2, int(current_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "college/case_list2.html", locals())

class CaseList3View(View):
    """
    显示投资学院-合作资源
    """
    def get(self,request):
        news_all = News.objects.only('id', 'title', "create_date").filter()[0:9]
        news_all_list = models.CooperativeResources.objects.only('id', 'title','image_url').filter()
        paginator = Paginator(news_all_list,12)
        page_num = request.GET.get("page",1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        current_page_num = page_of_news.number
        page_range = [x for x in range(int(current_page_num) - 2, int(current_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "college/case_list3.html", locals())

class CaseList4View(View):
    """
    显示投资学院-数据中心
    """
    def get(self,request):
        news_all = News.objects.only('id', 'title', "create_date").filter()[0:9]
        news_all_list = models.DataCenter.objects.only('id', 'title','image_url').filter()
        paginator = Paginator(news_all_list,12)
        page_num = request.GET.get("page",1)
        page_of_news = paginator.get_page(page_num)
        news = page_of_news.object_list
        current_page_num = page_of_news.number
        page_range = [x for x in range(int(current_page_num) - 2, int(current_page_num) + 3) if
                      0 < x <= paginator.num_pages]
        return render(request, "college/case_list4.html", locals())