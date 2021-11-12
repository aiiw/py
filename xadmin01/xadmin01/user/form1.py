# from django.forms import forms
from django import forms
from django.forms import ModelForm

from .models import DataSet,vsql


class getwc(forms.Form):
    names = forms.CharField(label="用户名:",strip="提示帮助")
    code=forms.CharField()
    tax=forms.CharField()
    sql=forms. CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows':1}))

class dbset(ModelForm):
    class Meta:
        model=DataSet
        fields="__all__"
        passwd = forms.CharField(widget=forms.PasswordInput)
        labels = {
            "id": "id",  # 用于html页面中显示的名字
            "dataset": "数据集名称1",
            "database": "数据库",
            "username": "用户账号",
            "passwd": "用户密码",
            "ip": "数据库地址",
            "inputdate": "创建时间",

        }
class dbsql(ModelForm):
    class Meta:
        model=vsql
        fields="__all__"
        # 重写modelform的init方法
        # def __init__(self, request, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #
        #     # 找到想要的字段，重新绑定显示的数据
        #     # 数据 = 数据库中获取
        #     total_data_list = [('', '---请选择---')]  # 父文章可以空，增加空选项
        #     data_list = models.Wiki.objects.filter(project=request.project).values_list('id', 'title')
        #     total_data_list.extend(data_list)
        #
        #     self.fields['parent'].choices = total_data_li




