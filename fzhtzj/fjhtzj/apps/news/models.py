from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class News(models.Model):
    """
    """
    title = models.CharField(max_length=150,verbose_name="标题", help_text="标题")
    tags = models.CharField(max_length=200, verbose_name="新闻类型", help_text="新闻类型")
    content = HTMLField()
    create_date = models.DateTimeField(auto_now=True, verbose_name="发布时间", help_text="发布时间")

    class Meta:
        ordering = ['-create_date', '-id']
        db_table = "tb_news"  # 指明数据库表名
        verbose_name = "新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title