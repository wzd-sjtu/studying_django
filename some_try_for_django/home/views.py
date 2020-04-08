from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from home.models import Reward
from person.models import Person
from item.models import Item
from .forms import RewardModeLForm
#  home在本质上是一种个人主页
# 查询相关API：

#  <1>filter(**kwargs):      它包含了与所给筛选条件相匹配的对象

#  <2>all():                 查询所有结果

#  <3>get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。

#-----------下面的方法都是对查询的结果再进行处理:比如 objects.filter.values()--------

#  <4>values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列 model的实例化对象，而是一个可迭代的字典序列
                                     
#  <5>exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象

#  <6>order_by(*field):      对查询结果排序

#  <7>reverse():             对查询结果反向排序

#  <8>distinct():            从返回结果中剔除重复纪录

#  <9>values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

#  <10>count():              返回数据库中匹配查询(QuerySet)的对象数量。

# <11>first():               返回第一条记录

# <12>last():                返回最后一条记录

#  <13>exists():             如果QuerySet包含数据，就返回True，否则返回False。



def index(request):
    # First Div
    #  通过all完成对数据的各种查询 这个objects.all本质上是调用数据库的一个接口
    last_person_post = Person.objects.all()[:1]
    last_item_post = Item.objects.all()[:1]
    # End First Div

    # 2nd Div
    lost_person = Person.objects.filter(person="L").all()[:1]
    lost_item = Item.objects.filter(category="L").all()[:1]
    # End 2 div

    # table
    #  这里的person属性和category属性都是一种类别的表示，是用来区分物件的存在
    recent_found_person = Person.objects.filter(person="F").all()[:3]
    recent_item_item = Item.objects.filter(category="F").all()

    # Reword Post
    my_reward = Reward.objects.    all()[:3]

    # Found Post Count Post
    a = Person.objects.filter(person="F").all()
    b = Item.objects.filter(category="F").all()

    # Lost Post Count
    c = Person.objects.filter(person="L").all()
    d = Item.objects.filter(category="L").all()


    #  这个是发送给html服务器的数据，在前端用来展示使用的
    context = {
        'lost_person': lost_person,
        'lost_item': lost_item,
        'recent_found_person': recent_found_person,
        'recent_found_item': recent_item_item,
        'my_reward': my_reward,

        # Total Post Count
        #  这个是所有的数据包？？ 发送的数据太大？
        'a': a,
        'b': b,
        'c': c,
        'd': d,

    }

    context['last_post'] = last_person_post
    context['last_post'] = last_item_post

    return render(request, 'index.html', context)


# Reward Function

def reward(request):
    if request.method == 'POST':
        form = RewardModeLForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        form = RewardModeLForm()
    context = {
        'form': form,
    }
    return render(request, 'reward.html', context)