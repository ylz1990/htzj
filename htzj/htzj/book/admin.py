from django.contrib import admin
# from .models import User,Bookinfo,Goldinfo,Newinfo
from .models import User,Bookinfo
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["id","author","title","pub_time"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

# class NewAdmin(admin.ModelAdmin):
#     list_display = ["id","author","title","pub_time"]
#
# class GoldAdmin(admin.ModelAdmin):
#     list_display = ["id","author","title","pub_time"]

admin.site.register(User,UserAdmin)
admin.site.register(Bookinfo,BookAdmin)
# admin.site.register(Goldinfo,GoldAdmin)
# admin.site.register(Newinfo,NewAdmin)

