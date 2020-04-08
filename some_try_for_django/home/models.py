from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

#  主要是存储用户的一些信息
class MyUser(AbstractUser):

    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )  # 性别选择
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M") #性别字段
    phone_number = models.CharField(max_length=15)  #手机号字段
    '''  DateTimeField和DateField和TimeField存储的内容分别对应着datetime(),date(),time()三个对象。

 对于auto_now=False和auto_now_add=False，两者默认值都为False。

  auto_now=Ture，字段保存时会自动保存当前时间，
  但要注意每次对其实例执行save()的时候都会将当前时间保存，
  也就是不能再手动给它存非当前时间的值。
  auto_now_add=True，
  字段在实例第一次保存的时候会保存当前时间，
  不管你在这里是否对其赋值。但是之后的save()是可以手动赋值的。
  也就是新实例化一个model，想手动存其他时间，
  就需要对该实例save()之后赋值然后再save()。 '''

    #       可以手动修改时间
    timestamp = models.DateTimeField(auto_now_add=True) #时间戳？

    #       不能自己修改时间
    update = models.DateTimeField(auto_now=True) #更新时间？

    #  当使用print输出对象时，会调用__str__(self)输出  类似于一种重载
    def __str__(self):
        return self.username
    #   作为嵌套类，主要是给上级增加一些功能，或者指定一系列标准
    class Meta:
        ordering = ["-update"]


class Reward(models.Model):
    #  奖励系信息？或者是对物品的描述性信息？？
    text = models.CharField(max_length=50)
    # 以下的时间戳服务器和之前是完全相同的
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text