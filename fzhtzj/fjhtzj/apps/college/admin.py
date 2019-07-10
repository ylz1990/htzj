from django.contrib import admin
from .models import RealTimeNews,ExpertComments,CooperativeResources,DataCenter
# Register your models here.

class RealTimeNewsAdmin(admin.ModelAdmin):
    list_display = ["id","title","create_date"]

class ExpertCommentsAdmin(admin.ModelAdmin):
    list_display = ["id","title","create_date"]

class CooperativeResourcesAdmin(admin.ModelAdmin):
    list_display = ["id","title","create_date"]

class DataCenterAdmin(admin.ModelAdmin):
    list_display = ["id","title","create_date"]

admin.site.register(RealTimeNews,RealTimeNewsAdmin)
admin.site.register(ExpertComments,ExpertCommentsAdmin)
admin.site.register(CooperativeResources,CooperativeResourcesAdmin)
admin.site.register(DataCenter,DataCenterAdmin)