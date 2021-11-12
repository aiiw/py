from django.test import TestCase

# Create your tests here.
"""向浏览器返回真正的HTML响应，添加一个新的测试方法"""


from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import tag


class HomePageTest(TestCase):

    def test_root_url_to_home_page(self):
        found = resolve('/')  # resolve是Django内部函数，用于解析URL，并将其映射到相应的视图函数上
        self.assertEqual(found.func, tag)  # 检查解析网站根路径/时，是否能找到home_page

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # 1
        response = tag(request)  # 2
        html = response.content.decode('utf8')  # 3
        self.assertTrue(html.startswith('<html>'))  # 4
        self.assertIn('<title>To-Do lists</title>', html)  # 5
        self.assertTrue(html.endswith('</html>'))  # 4

"""
代码解析：
    1、我们创建了一个Httprequest对象，用户在浏览器请求网页时，Django看到的就是Httprequest请求
    2、把这个HttpRequest对象传给home_page视图，得到响应，响应对象为 HttpResponse类的实例，响应的.content属性中有特定的内容
    3、响应的.content这些原始字节将被发送到用户的浏览器，我们通过.decode()将它们转换后发送到用户
    4、他以一个<html>标记开始，该标记在结尾处关闭
    5、希望在中间的某一个地方有一个<title>标签，含to_do单词，这是我们在功能测试中指定的。
"""
"""
单元测试：
    在终端执行# python manage.py test
        TypeError: home_page() takes 0 positional arguments but 1 was given
"""