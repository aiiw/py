import time

import arrow as arrow
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from pymysql.cursors import DictCursor
from django_redis import get_redis_connection
import redis
from mysarly.models import Salary01
from user import models
from xadmin01.oauser import StudentList


def r1(request):

    try:
        all_book = Salary01.objects.all().order_by('-id')
        if not all_book:
            return HttpResponse('书籍信息表为空，请录入！')
    except Exception as e:
        print(e)
    # return render(request, 'mysarly.html', locals()) 直接将所有的变量传递,效果同下
    return render(request, 'mysarly.html', {'all_book':all_book})

@login_required
def r2(request):
    try:
        all_book = Salary01.objects.all().order_by('-id')
        if not all_book:
            return HttpResponse('书籍信息表为空，请录入！')
    except Exception as e:
        print(e)

    paginator = Paginator(all_book, 18)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    # return render(request, 'mysarly.html', locals()) 直接将所有的变量传递,效果同下
    return render(request, 'mysarly01.html', locals())

def mssql(request):
    import sys
    sys.path.append("..")
    print(sys.path)
    import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
    serverName = '192.168.0.128'
#登陆用户名和密码
    userName = 'sa'
    passWord = '$u2930123WJ'
#建立连接并获取cursor
    conn = pymssql.connect(serverName , userName , passWord, "Card3500")
    cursor = conn.cursor()
    # cursor = conn.cursor(DictCursor)

# 查询记录
#     cursor.execute('select * from cardlist')
# # 获取一条记录
#     row = cursor.fetchone()
# # 循环打印记录(这里只有一条，所以只打印出一条)
#     while row:
#         print("ID=%s, Name=%s" % (row[0], row[1]))
#         row = cursor.fetchone()
# # 连接用完后记得关闭以释放资源
    cursor.execute('select * from cardlist')
    all_rs =cursor.fetchall()

    # a=input()
    paginator = Paginator(all_rs, 18)
    conn.close()
    return render(request, 'sqlrs.html', locals())
@cache_page(60 * 1)
def testcatche(request):
    conn = get_redis_connection("default")
    t1 = arrow.now() # 得到当前时间戳
    time.sleep(10)  # 阻塞三秒
    html = 't1 is %s' % (t1)
    return HttpResponse(html)

def student(request):

    if request.method == 'GET':
        student_list = StudentList()
        return render(request,'student.html',{'student_list':student_list})
    else:

        student_list = StudentList(request.POST)

        if student_list.is_valid():
            print(student_list)
            student_list.save()
            return HttpResponse("数据提交成功！！")
        return redirect(request, 'student_list.html', {'student_list': student_list})


def test1(request):
    from time import sleep
    sleep(1000)
    print("aaaaaaaaaaaaaaaaaaaaaa")
    return HttpResponse("测试框架是否同步执行")