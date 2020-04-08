from django import forms
from .models import Reward

#  form是在处理上传数据的中转平台  这点要谨记
class RewardModeLForm(forms.ModelForm):

    #  这个Meta类是为了引用models里面的字段来进行使用的  可以直接修改models的字段
    class Meta:
        model = Reward
        #  引用的是Reward里面的text
        fields = [
            'text'
        ]