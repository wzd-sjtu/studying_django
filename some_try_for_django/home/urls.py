from django.urls import path
from . import views


#  在这里建立连接链接

urlpatterns = [
    path('', views.index, name='index'),
    path('reward/', views.reward, name='reward')
]