from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyUser, Reward

# Register your models here.

#  在数据库管理员界面增加上这几个模型的特点
admin.site.register(MyUser)
admin.site.register(Reward)
