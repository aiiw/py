import json

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import cache_page

from django.views.decorators.csrf import csrf_exempt

from xadmin.views import CommAdminView


from . import form1
# 这个[设置信息源]是提交
class setdb(CommAdminView):
    def get(self, request):
        obj = form1.dbset()
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "设置信息源"  # 定义面包屑变量
        # context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        context["db"] = obj
        from .models import DataSet
        heads = DataSet._meta.fields
        print(heads)
        t1=[heads[i].name for i in range(len(heads))]
        t2=[DataSet._meta.get_field(j).verbose_name for j in t1]
        dict1=dict(zip(t1,t2))
        print(dict1)

        # from . import getfield
        # ghead = getfield.gethead("select * from dataset")
        context["thead"] = dict1
        return render(request, 'setdb.html', context)  # 最后指定自定义的template模板，并返回context

    @csrf_exempt  # 在这里暂时不起作用
    def post(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "设置信息源"  # 定义面包屑变量
        # context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        context["thead"]=""
        obj = form1.dbset(request.POST)
        from .models import DataSet
        heads = DataSet._meta.fields
        q1 = request.POST.get('dataset')
        dbset=DataSet.objects.filter(dataset=q1)
        print(dbset.count())

        if obj.is_valid() and dbset.count()<1 :
            obj.save()
        else:
            pass
        context["db"] = obj
        # from . import getfield
        # ghead = getfield.gethead("select * from dataset")

        t1 = [heads[i].name for i in range(len(heads))]
        t2 = [DataSet._meta.get_field(j).verbose_name for j in t1]
        dict1 = dict(zip(t1, t2))
        print(dict1)
        context["thead"] = dict1
        return render(request, 'setdb.html', context)
# 这个[设置信息源]是编辑
def updatadb(request):
    # return render(request, 'testtag.html')
    from .models import DataSet
    dataset=request.POST.get('dataset')
    print(dataset)
    p=DataSet.objects.get(dataset=dataset)
    obj = form1.dbset(request.POST,instance=p)

    obj.save()
    return HttpResponse("修改成功~~")
# 这个[设置信息源]是删除
def deldb(request):
    from .models import DataSet
    dataset = request.POST.get('dataset')
    p = DataSet.objects.get(dataset=dataset)
    p.delete()
    return HttpResponse("删除成功~~")
# 2这个[脚本信息录入]提交
class edit_sql(CommAdminView):
    def get(self, request):
        from .models import vsql
        obj = form1.dbsql()
        context = super().get_context();
        title = "脚本信息录入";
        context["title"] = title  # 把面包屑变量添加到context里面
        context["editsql"]=obj
        #edit by 20211013
        from .models import vsql
        heads = vsql._meta.fields
        print("vsql._meta.fields",heads)
        t1 = [heads[i].name for i in range(len(heads))]
        t2 = [vsql._meta.get_field(j).verbose_name for j in t1]
        dict1 = dict(zip(t1, t2))
        print(dict1)
        # from . import getfield
        # ghead = getfield.gethead("select * from dataset")
        context["thead"] = dict1
        return render(request, 'sql.html', context)
    def post(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "脚本信息录入"  # 定义面包屑变量
        # context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        context["thead"]=""

        from .models import vsql
        heads = vsql._meta.fields

        q1 = request.POST.get('id')


        obj = form1.dbsql(request.POST)

        if obj.is_valid() and q1!="" :
            obj.save()
            pass
        else:
            pass
        context["editsql"] = obj
        # from . import getfield
        # ghead = getfield.gethead("select * from dataset")

        t1 = [heads[i].name for i in range(len(heads))]
        t2 = [vsql._meta.get_field(j).verbose_name for j in t1]
        dict1 = dict(zip(t1, t2))
        print(dict1)
        context["thead"] = dict1
        return render(request, 'sql.html', context)

def upsql(request):
    # return render(request, 'testtag.html')
    from .models import vsql
    id=request.POST.get('id')
    p=vsql.objects.get(id=id)
    dict1=dict(request.POST)
    dict1.pop('id')
    print(dict1)

    obj = form1.dbsql(request.POST,instance=p)
    # p.title=request.POST.get('title')
    #
    obj.save()
    return HttpResponse("修改成功~~")
# 这个[设置信息源]是删除
def delsql(request):
    from .models import vsql
    id = request.POST.get('id')
    p = vsql.objects.get(id=id)
    p.delete()
    return HttpResponse("删除成功~~")




class dbset(CommAdminView):
    def get(self, request):
        obj =form1.getwc()
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "自定义报表"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        context["wc"]=obj
        print(type(context["wc"]))


        return render(request, 'test.html',context)  # 最后指定自定义的template模板，并返回context

    @csrf_exempt #在这里暂时不起作用
    def post(self,request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "自定义报表"  # 定义面包屑变量
        # context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面


        obj = form1.getwc(request.POST)
        if obj.is_valid():
            context["wc"] = obj
            data = obj.clean()
            sql=data['sql']
            from . import getfield
            ghead=getfield.gethead(sql)

            context["thead"] = ghead


        else:
            error_msg = obj.errors
            context["err"] = error_msg
            context["thead"]=list
        return render(request, 'test.html', context)


# @cache_page(15)#这里加了缓存之后产生了一个问题,在添加记录后没有马上看到结果,所以屏蔽
def getsqlval(request):
    sql=request.GET.get("sql")
    if  sql  and  sql !='None':
        from urllib.parse import unquote
        import html
        sql=html.unescape(sql)
        from . import getfield
        values = getfield.getvalue(sql)
        return HttpResponse(values)

    else:
        return HttpResponse("none11")

def getsqlval2(request):
    # sql=request.GET.get("sql")
    from .getfield import DateEncoder
    from .models import vsql
    objs=vsql.objects.values()
    val=vsql.objects.values('dataset__id')
    print(val)

    result = {}
    list1 = []
    result["total"] = objs.count()

    for obj in objs:
        list1.append(obj)
    result["rows"]=list1
    results = json.dumps(result, cls=DateEncoder)

    if  objs.count()>1:
        return HttpResponse(results)
    else:
        return HttpResponse("none11")

def tag(request):
    return render(request,'testtag.html')

class tool(CommAdminView):
    def get(self, request):
        from .models import vsql
        context = super().get_context();
        title = "脚本信息录入2";
        context["title"] = title  # 把面包屑变量添加到context里面

        return render(request, 'j1.html', context)


def resql(request):
    import re
    str1=request.POST.get("mystr")
    id=request.POST.get("id")
    if id=="1":#提交T100脚本
        p1 = re.compile(r'(",)|(")|#.+|g_dlang|\|')
        #p2 = re.compile('\s')
        reset1 = p1.sub("", str1)
        p2=re.compile((r'\?'))
        reset2=p2.sub("''",reset1)

        #reset3 = reset2.replace("''", "'")
        return HttpResponse(reset2)
    elif id=="2":#提交数据加""
        p1 = re.compile(r'^|$')
        p2 = re.compile('\s')
        reset1 = p1.sub("'", str1)
        reset2 = p2.sub("','", reset1)
        reset3 = reset2.replace("''", "'")
        return HttpResponse(reset3)

def sendoa(request):
    from .sendoa import sendoa
    str=request.GET.get('str')
    id=request.GET.get('id')
    print(id)
    sendoa(str,id)
    return  HttpResponse("发送成功")




