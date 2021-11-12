import xadmin
from .models import EmailVerifyRecord,AutoUser,Department,Emp
#oa
class listoa():
    list_display=['user_name','byname','user_priv_name','birthday','mobil_no','bp_no','email','last_visit_time','last_pass_time','last_visit_ip','uid']
    search_fields = ['user_name','byname','user_priv_name','birthday','mobil_no','bp_no','email','last_visit_time','last_pass_time','last_visit_ip','weather_city']
    list_filter = ['user_name','byname','user_priv_name','birthday','mobil_no','bp_no','email','last_visit_time','last_pass_time','last_visit_ip','weather_city']
    fields_set=[(u'基本信息',{'fields':['user_name','byname','user_priv_name','birthday','mobil_no','bp_no','email','last_visit_time','last_pass_time','last_visit_ip','weather_city']})]
    show_detail_fields = ['last_visit_ip']
    # refresh_times = (3,5)     # 数据刷新时间

    # data_charts = {
    #     "user_count": {'title': u"约运动",
    #                    "x-field": "user_name",
    #                    "y-field": ("birthday",),
    #                    },
    # }
    # list_per_page = 10
    # # 相应表图标配置
    # # https://fontawesome.com/icons
    # model_icon = 'fa fa-address-book'
    # 执行动作框的位置
    # actions_on_top = True
    # actions_on_bottom = True
xadmin.site.register(AutoUser, listoa)
class emp1():
    list_display=['id','code','name','identitynumber','jobrankid','nationcode','birthday','phone','qq','email','sex','hiredate']
    search_fields=['code','name','identitynumber']
    fields_set = [(u'基本信息', {
        'fields': ['user_name', 'byname', 'user_priv_name', 'birthday', 'mobil_no', 'bp_no', 'email', 'last_visit_time',
                   'last_pass_time', 'last_visit_ip', 'weather_city']})]

xadmin.site.register(Emp,emp1)
class EmailVerifyRecordAdmin():
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    fields_set =(u'基本信息', {
        'fields': ['code', 'email']})


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

xadmin.site.register(Department)
from xadmin import views


class BaseSetting(object):
    #开启主题选择
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    site_title = "万事泰集团后台管理系统"
    site_footer = "http://www.mastergroup.com.cn"
    menu_style = "accordion"  # 设置菜单折叠

    def get_site_menu(self):  # 名称不能改
        return [
            {
                'title': '报表模块',
                'icon': '',
                'menus': (
                    {
                        'title': '填写服务器信息',
                        'url': '/xadmin/setdb',
                        'icon': 'fa fa-bar-chart-o'
                    },
                    {
                        'title': '脚本信息录入',  # 这里是你菜单的名称
                        'url': '/xadmin/sql',  # 这里填写你将要跳转url
                        'icon': 'fa fa-bar-chart-o'  # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                    {
                        'title': '自定义报表',  # 这里是你菜单的名称
                        'url': '/xadmin/test_view',  # 这里填写你将要跳转url
                        'icon': 'fa fa-bar-chart-o'  # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                )
            },
            {
                'title': '日常使用',
                'icon': '',
                'menus': (
                    {
                        'title': '常用工具',
                        'url': '/xadmin/tool',
                        'icon': 'fa fa-bar-chart-o'
                    },

                )
            },


        ]

#注册你上面填写的url
from .views import dbset,setdb,edit_sql,tool   #从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理
xadmin.site.register_view(r'setdb/$', setdb, name='setdb')
xadmin.site.register_view(r'sql/$', edit_sql, name='vsql')
xadmin.site.register_view(r'test_view/$', dbset, name='for_test')
xadmin.site.register_view(r'tool/$', tool, name='for_test')

xadmin.site.register(views.CommAdminView, GlobalSetting)


from django.apps import AppConfig
class HomeConfig(AppConfig):
    name = 'home'
    verbose_name = '我的首页'