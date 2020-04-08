from django.db import models

# Create your models here.
from django.db import models
from home.models import MyUser


# Create your models here.

#   专门为了一个类开了一个app？？

#  在这里生成一个人的所有信息？？详细信息？
class Person(models.Model):
    status = models.CharField(max_length=60)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")

    PERSON_CHOICES = (
        ('F', 'Found Person'),
        ('L', 'Lost Person'),
    )
    person = models.CharField(max_length=1, choices=PERSON_CHOICES, default="Found Item")
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    body_color = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=16)
    image = models.FileField()
    identification_mark = models.TextField(help_text='Separate each item by comma')
    secret_information = models.TextField(help_text='Separate each item by comma')
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    #  按照更新顺序进行排列？？
    class Meta:
        ordering = ["-update"]
    #  给person类增加的内部调用类   类似于数据传递
    def get_contents(self):
        #  将不同的数据用，进行分割
        return self.identification_mark.split(",")
    #   与上面是同理的
    def get_excludes(self):
        return self.secret_information.split(",")
