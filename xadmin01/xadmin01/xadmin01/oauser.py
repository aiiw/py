from django.forms import ModelForm

from user import models


class StudentList(ModelForm):
    class Meta:
        model = models.AutoUser  #对应的Model中的类
        fields = "__all__"      #字段，如果是__all__,就是表示列出所有的字段
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
#error_messages用法：
        error_messages = {
            'name':{'required':"用户名不能为空",},
        }

#widgets用法,比如把输入用户名的input框给为Textarea
#首先得导入模块
        from django.forms import widgets as wid  #因为重名，所以起个别名
        widgets = {
            "name":wid.Textarea(attrs={"class":"c1"}) ,#还可以自定义属性 email
            "email": wid.EmailInput(attrs={'class': 'form-control'}),
        }
#labels，自定义在前端显示的名字

    labels= {
            "name":"用户名"
        }