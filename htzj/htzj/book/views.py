from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
# from .models import Bookinfo,User,Goldinfo,Newinfo
from .models import Bookinfo,User
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def test1(request):
    return HttpResponse("hello book")

# 主页
def htzj(request):
    context = {}
    blog_list = Bookinfo.objects.filter().order_by("-pub_time")
    context['blog_list'] = blog_list

    return render(request,"htzj/index.html",context)


# 关于
def about(request):
    return render(request,"htzj/about.html")

def about_1(request):
    return render(request,"htzj/about_1.html")

def about_2(request):
    return render(request,"htzj/about_2.html")
# 案件
def case(request):
    return render(request,"htzj/Case.html")

def contant(request):
    return render(request,"htzj/Contant.html")

def downlist(request):
    return render(request,"htzj/DownList.html")

def download(request):
    name = request.POST.get("userid")
    password = request.POST.get("pwd")
    user = User.objects.filter(name=name,passwords=password)
    if user:
        request.session["name"] = name
        return redirect(reverse("add"))
    else:
        return render(request,"htzj/DownLoad.html")

# 文章详情页
def newlist(request,blog_id):
    blog = Bookinfo.objects.get(id=blog_id)
    return render(request,"htzj/NewList.html",context={"blog":blog})

def news(request):
    context = {}
    blog_list = Bookinfo.objects.all().order_by("-pub_time")
    page_robot = Paginator(blog_list, 10)
    try:
        blog_list = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list = page_robot.page(1)
    except EmptyPage:
        blog_list = page_robot.page(page_robot.num_pages)
    context['blog_list'] = blog_list
    return render(request,"htzj/News.html",context)

# 新闻资讯的页面
def news_1(request):
    context = {}
    blog_list1 = Bookinfo.objects.filter(new_type__contains="['新闻资讯']").order_by("-pub_time")
    page_robot = Paginator(blog_list1, 10)
    try:
        blog_list1 = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list1 = page_robot.page(1)

    except EmptyPage:
        blog_list1 = page_robot.page(page_robot.num_pages)
    context['blog_list1'] = blog_list1
    return render(request,"htzj/News_1.html",context)

# 行业资讯的页面
def news_2(request):
    context = {}
    blog_list1 = Bookinfo.objects.filter(new_type__contains="['行业资讯']").order_by("-pub_time")
    page_robot = Paginator(blog_list1, 10)
    try:
        blog_list1 = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list1 = page_robot.page(1)

    except EmptyPage:
        blog_list1 = page_robot.page(page_robot.num_pages)
    context['blog_list1'] = blog_list1
    return render(request,"htzj/News_2.html",context)

# 黄金资讯的页面
def news_3(request):
    context = {}
    blog_list1 = Bookinfo.objects.filter(new_type__contains="['黄金资讯']").order_by("-pub_time")
    page_robot = Paginator(blog_list1, 10)
    try:
        blog_list1 = page_robot.page(request.GET.get("page"))
    except PageNotAnInteger:
        blog_list1 = page_robot.page(1)

    except EmptyPage:
        blog_list1 = page_robot.page(page_robot.num_pages)
    context['blog_list1'] = blog_list1
    return render(request,"htzj/News_3.html",context)

def products(request):
    return render(request,"htzj/products.html")

# 黄金T+D
def product_list(request):
    return render(request,"htzj/product_List.html")

# 纸黄金
def gold_college2(request):
    return render(request,"htzj/gold_college_2.html")

# COMEX黄金
def gold_college3(request):
    return render(request,"htzj/gold_college_3.html")

# 伦敦金
def gold_college4(request):
    return render(request,"htzj/gold_college_4.html")

# 金条
def gold_college5(request):
    return render(request,"htzj/gold_college_5.html")

# 贵金属
def gold_college6(request):
    return render(request,"htzj/gold_college_6.html")

# 投资技巧
def gold_college7(request):
    return render(request,"htzj/gold_college_7.html")

# 黄金投资
def gold_college8(request):
    return render(request,"htzj/gold_college_8.html")

# 黄金学堂
def gold_college9(request):
    return render(request,"htzj/gold_college_9.html")



#  添加文章的视图函数
# def add(request):
#     return render(request,"htzj/add.html")

# def add_handle(request):
#     author = request.POST.get("author")
#     title = request.POST.get("title")
#     pub_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
#     content = request.POST.get("content")
#     new_type = request.POST.getlist("new_type")
#     if new_type[0] == "新闻资讯":
#         user_id = 1
#         blog = Bookinfo(title=title, author=author, content=content, pub_time=pub_time, user_id=user_id, new_type=new_type)
#         blog.save()
#     elif new_type[0] == "行业资讯":
#         blog = Newinfo(title=title, author=author, content=content, pub_time=pub_time, new_type=new_type)
#         blog.save()
#     else:
#         blog = Goldinfo(title=title, author=author, content=content, pub_time=pub_time, new_type=new_type)
#         blog.save()
#     print(author)
#     print(new_type)
#     return redirect(reverse("add"))
# def add_handle(request):
#     author = request.POST.get("author")
#     title = request.POST.get("title")
#     pub_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
#     content = request.POST.get("content")
#     new_type = request.POST.getlist("new_type")
#     blog = Bookinfo(title=title, author=author, content=content, pub_time=pub_time, new_type=new_type)
#     blog.save()
#     return redirect(reverse("add"))

# 用于文章的修改和删除
# def edit(request):
#     context = {}
#     blog_list = Bookinfo.objects.all().order_by("-pub_time")
#     page_robot = Paginator(blog_list, 10)
#     try:
#         blog_list = page_robot.page(request.GET.get("page"))
#     except PageNotAnInteger:
#         blog_list = page_robot.page(1)
#     except EmptyPage:
#         blog_list = page_robot.page(page_robot.num_pages)
#     context['blog_list'] = blog_list
#     return render(request, "htzj/edit.html", context)
#
# # 文章删除
# def delete(request,blog_id):
#     blog = Bookinfo.objects.get(id=blog_id)
#     if blog:
#         blog.delete()
#         return redirect(reverse('edit'))
#     else:
#         return HttpResponse("操作失败")
#
# # 文章修改
# def alter(request,blog_id):
#     blog = Bookinfo.objects.get(id=blog_id)
#     if request.method == "GET":
#         return render(request,'htzj/alter.html',context={"blog":blog})
#     elif request.method == "POST":
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         content = request.POST.get('content')
#         blog.title = title
#         blog.author = author
#         blog.content = content
#         blog.save()
#         return redirect(reverse('edit'))
#     else:
#         return HttpResponse("操作失败，请重新编辑")

# 添加用户
# def user(request):
#     user = User()
#     user.name = "wangwu"
#     user.passwords = "htzj123456"
#     user.save()
#     return HttpResponse("用户添加成功")
