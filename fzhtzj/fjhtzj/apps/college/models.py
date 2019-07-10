from django.db import models
from tinymce.models import HTMLField
# Create your models here.

# 显示投资学院-实时快讯
class RealTimeNews(models.Model):
    """
    """
    title = models.CharField(max_length=150,verbose_name="标题", help_text="标题")
    # image_url = models.URLField(default="", verbose_name="图片url", help_text="图片url")
    image_url = models.ImageField(upload_to='img', default="", blank=True)  # upload_to指定图片上传的途径，如果不存在则自动创建
    content = HTMLField()
    create_date = models.DateTimeField(auto_now=True, verbose_name="发布时间", help_text="发布时间")

    class Meta:
        ordering = ['-create_date', '-id']
        db_table = "RT_news"  # 指明数据库表名
        verbose_name = "实时快讯"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title


# 显示投资学院-专家点评

class ExpertComments(models.Model):
    title = models.CharField(max_length=150, verbose_name="标题", help_text="标题")
    image_url = models.ImageField(upload_to='img',default="",blank=True) # upload_to指定图片上传的途径，如果不存在则自动创建
    content = HTMLField()
    create_date = models.DateTimeField(auto_now=True, verbose_name="发布时间", help_text="发布时间")

    class Meta:
        ordering = ['-create_date', '-id']
        db_table = "EP_comm"  # 指明数据库表名
        verbose_name = "专家点评"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title

# 显示投资学院-数据中心
class  DataCenter(models.Model):
    title = models.CharField(max_length=150, verbose_name="标题", help_text="标题")
    image_url = models.ImageField(upload_to='img',default="",blank=True) # upload_to指定图片上传的途径，如果不存在则自动创建
    content = HTMLField()
    create_date = models.DateTimeField(auto_now=True, verbose_name="发布时间", help_text="发布时间")

    class Meta:
        ordering = ['-create_date', '-id']
        db_table = "DC_table"  # 指明数据库表名
        verbose_name = "数据中心"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title

# 显示投资学院-合作资源
class CooperativeResources(models.Model):
    title = models.CharField(max_length=150, verbose_name="标题", help_text="标题")
    image_url = models.ImageField(upload_to='img',default="",blank=True) # upload_to指定图片上传的途径，如果不存在则自动创建
    content = HTMLField()
    create_date = models.DateTimeField(auto_now=True, verbose_name="发布时间", help_text="发布时间")

    class Meta:
        ordering = ['-create_date', '-id']
        db_table = "CR_table"  # 指明数据库表名
        verbose_name = "合作资源"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title