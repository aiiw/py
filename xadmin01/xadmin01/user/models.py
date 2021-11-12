# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


# Create your models here.
class DataSet(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    dataset = models.CharField(db_column='dataset',default='其它数据库',max_length=100, verbose_name=u'数据集')
    database=models.CharField(db_column='database',max_length=100, blank=True, null=True, verbose_name=u'数据库名称')
    username= models.CharField(db_column='username',max_length=100, blank=True, null=True, verbose_name=u'用户名')
    passwd = models.CharField(db_column='passwd', max_length=100, blank=True, null=True, verbose_name=u'密码')
    ip=models.CharField(db_column='ip',max_length=100, blank=True, null=True, verbose_name=u'服务器地址')

    inputdate = models.DateTimeField(db_column='inputdate', blank=True, null=True, default=datetime.now,verbose_name=u'录入时间')
    remark=models.CharField(db_column='remark',max_length=100, blank=True, null=True, verbose_name=u'备注')
    class Meta:
        db_table = 'dataset'
        verbose_name = '数据集信息'
        verbose_name_plural = '数据集信息'
        managed = False
    def __str__(self):
        return self.dataset

class vsql(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title=models.CharField(db_column='title',max_length=100, verbose_name=u'标题')
    inputdate = models.DateTimeField(db_column='inputdate', blank=True, null=True, default=datetime.now,verbose_name=u'录入时间')
    remark=models.CharField(db_column='remark',max_length=100, blank=True, null=True, verbose_name=u'备注')
    dataset = models.ForeignKey("DataSet",on_delete=models.CASCADE,related_name='sql',verbose_name=u'数据集')
    sql = models.TextField(db_column='sql', max_length=500, blank=True, null=True, verbose_name=u'脚本')
    class Meta:
        db_table = 'vsql'
        verbose_name = '数据脚本'
        verbose_name_plural = '数据脚本'



class Department(models.Model):
    depart_name = models.CharField(max_length=20, verbose_name='所属部门')
    depart_group = models.CharField(max_length=20, blank=True, null=True, verbose_name='部门小组')

    class Meta:
        verbose_name = u'部门信息'
        verbose_name_plural = verbose_name
        managed = False

    def __unicode__(self):
        return self.depart_name



class UserProfile(models.Model):
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name='性别')
    address = models.CharField(max_length=100, default=u'', null=True, blank=True, verbose_name='地址')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    department = models.ForeignKey(Department, verbose_name='部门',on_delete=None)

    class Meta:
        verbose_name = u'用户信息'
        managed = False
    def __unicode__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')
    class Meta:
        verbose_name = u'验证信息'
        managed = False
    def __unicode__(self):
        return self.code

class AutoUser(models.Model):
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=60, blank=True, null=True,verbose_name=u'用户名')  # Field name made lowercase.
    user_name_index = models.CharField(db_column='USER_NAME_INDEX', max_length=60, blank=True, null=True)  # Field name made lowercase.
    byname = models.CharField(db_column='BYNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    useing_key = models.CharField(db_column='USEING_KEY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    using_finger = models.CharField(db_column='USING_FINGER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key_sn = models.CharField(db_column='KEY_SN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secure_key_sn = models.CharField(db_column='SECURE_KEY_SN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_priv = models.IntegerField(db_column='USER_PRIV', blank=True, null=True)  # Field name made lowercase.
    user_priv_no = models.IntegerField(db_column='USER_PRIV_NO', blank=True, null=True)  # Field name made lowercase.
    user_priv_name = models.CharField(db_column='USER_PRIV_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    post_priv = models.CharField(db_column='POST_PRIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    post_dept = models.TextField(db_column='POST_DEPT', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.IntegerField(db_column='DEPT_ID', blank=True, null=True)  # Field name made lowercase.
    dept_id_other = models.CharField(db_column='DEPT_ID_OTHER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    view_dept_id = models.CharField(db_column='VIEW_DEPT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    view_uid = models.CharField(db_column='VIEW_UID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    view_priv_id = models.CharField(db_column='VIEW_PRIV_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leave_dept = models.IntegerField(db_column='LEAVE_DEPT', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    is_lunar = models.CharField(db_column='IS_LUNAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tel_no_dept = models.CharField(db_column='TEL_NO_DEPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax_no_dept = models.CharField(db_column='FAX_NO_DEPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    add_home = models.CharField(db_column='ADD_HOME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    post_no_home = models.CharField(db_column='POST_NO_HOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel_no_home = models.CharField(db_column='TEL_NO_HOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobil_no = models.CharField(db_column='MOBIL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bp_no = models.CharField(db_column='BP_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oicq_no = models.CharField(db_column='OICQ_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icq_no = models.CharField(db_column='ICQ_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msn = models.CharField(db_column='MSN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    avatar = models.CharField(db_column='AVATAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    call_sound = models.IntegerField(db_column='CALL_SOUND', blank=True, null=True)  # Field name made lowercase.
    last_visit_time = models.DateTimeField(db_column='LAST_VISIT_TIME', blank=True, null=True)  # Field name made lowercase.
    sms_on = models.CharField(db_column='SMS_ON', max_length=1, blank=True, null=True)  # Field name made lowercase.
    menu_type = models.CharField(db_column='MENU_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_pass_time = models.DateTimeField(db_column='LAST_PASS_TIME', blank=True, null=True)  # Field name made lowercase.
    theme = models.IntegerField(db_column='THEME', blank=True, null=True)  # Field name made lowercase.
    shortcut = models.TextField(db_column='SHORTCUT', blank=True, null=True)  # Field name made lowercase.
    portal = models.CharField(db_column='PORTAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    panel = models.CharField(db_column='PANEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    online = models.IntegerField(db_column='ONLINE', blank=True, null=True)  # Field name made lowercase.
    on_status = models.CharField(db_column='ON_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    attend_status = models.CharField(db_column='ATTEND_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mobil_no_hidden = models.CharField(db_column='MOBIL_NO_HIDDEN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mytable_left = models.CharField(db_column='MYTABLE_LEFT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mytable_right = models.CharField(db_column='MYTABLE_RIGHT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_priv_other = models.CharField(db_column='USER_PRIV_OTHER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_no = models.IntegerField(db_column='USER_NO', blank=True, null=True)  # Field name made lowercase.
    not_login = models.IntegerField(db_column='NOT_LOGIN', blank=True, null=True)  # Field name made lowercase.
    not_view_user = models.CharField(db_column='NOT_VIEW_USER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    not_view_table = models.CharField(db_column='NOT_VIEW_TABLE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    not_search = models.CharField(db_column='NOT_SEARCH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bkground = models.CharField(db_column='BKGROUND', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bind_ip = models.CharField(db_column='BIND_IP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    last_visit_ip = models.CharField(db_column='LAST_VISIT_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    menu_image = models.CharField(db_column='MENU_IMAGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    weather_city = models.CharField(db_column='WEATHER_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    show_rss = models.CharField(db_column='SHOW_RSS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    my_rss = models.TextField(db_column='MY_RSS', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    menu_expand = models.CharField(db_column='MENU_EXPAND', max_length=4, blank=True, null=True)  # Field name made lowercase.
    my_status = models.CharField(db_column='MY_STATUS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    limit_login = models.CharField(db_column='LIMIT_LOGIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='PHOTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    im_range = models.IntegerField(db_column='IM_RANGE', blank=True, null=True)  # Field name made lowercase.
    leave_time = models.DateTimeField(db_column='LEAVE_TIME', blank=True, null=True)  # Field name made lowercase.
    secret_level = models.IntegerField(db_column='SECRET_LEVEL', blank=True, null=True)  # Field name made lowercase.
    user_para = models.TextField(db_column='USER_PARA', blank=True, null=True)  # Field name made lowercase.
    not_mobile_login = models.IntegerField(db_column='NOT_MOBILE_LOGIN', blank=True, null=True)  # Field name made lowercase.
    manage_module_type = models.CharField(db_column='MANAGE_MODULE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_priv_type = models.IntegerField(db_column='USER_PRIV_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_manage_orgs = models.CharField(db_column='USER_MANAGE_ORGS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    device_number = models.CharField(db_column='DEVICE_NUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobil_no_bd = models.CharField(db_column='MOBIL_NO_BD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    corp_id = models.CharField(max_length=38, blank=True, null=True)
    theme_colour = models.CharField(db_column='THEME_COLOUR', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_user'
        verbose_name = 'OA用户'
        verbose_name_plural='OA用户'
    # def __unicode__(self):
    #     return self.user_name
    def __str__(self):  #这个才生产,上一个是无效的
        return self.user_name

class Emp(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True,verbose_name=u'用户ID')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True,verbose_name=u'员工编码')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True,verbose_name=u'用户姓名')  # Field name made lowercase.
    identitynumber = models.CharField(db_column='IdentityNumber', max_length=20, blank=True, null=True,verbose_name=u'身份证')  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True,verbose_name=u'部门ID')  # Field name made lowercase.
    jobrankid = models.IntegerField(db_column='JobRankID', blank=True, null=True,verbose_name=u'职级')  # Field name made lowercase.
    nationcode = models.CharField(db_column='NationCode', max_length=10, blank=True, null=True,verbose_name=u'籍贯')  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True,verbose_name=u'出生日期')  # Field name made lowercase.
    phone = models.CharField(max_length=100, blank=True, null=True,verbose_name=u'手机号码')
    qq = models.CharField(max_length=50, blank=True, null=True,verbose_name=u'QQ号码')
    email = models.CharField(max_length=50, blank=True, null=True,verbose_name=u'邮箱地址')
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True,verbose_name=u'性别')  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True,verbose_name=u'入职日期')  # Field name made lowercase.i

    class Meta:
        managed = False
        db_table = 'emp'
        verbose_name = '人员信息'
        verbose_name_plural = '人员信息'