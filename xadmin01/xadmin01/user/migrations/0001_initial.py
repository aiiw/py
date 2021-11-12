# Generated by Django 2.2.5 on 2021-10-13 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, db_column='UID', null=True)),
                ('user_id', models.CharField(blank=True, db_column='USER_ID', max_length=40, null=True)),
                ('user_name', models.CharField(blank=True, db_column='USER_NAME', max_length=60, null=True, verbose_name='用户名')),
                ('user_name_index', models.CharField(blank=True, db_column='USER_NAME_INDEX', max_length=60, null=True)),
                ('byname', models.CharField(blank=True, db_column='BYNAME', max_length=20, null=True)),
                ('useing_key', models.CharField(blank=True, db_column='USEING_KEY', max_length=1, null=True)),
                ('using_finger', models.CharField(blank=True, db_column='USING_FINGER', max_length=1, null=True)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=50, null=True)),
                ('key_sn', models.CharField(blank=True, db_column='KEY_SN', max_length=20, null=True)),
                ('secure_key_sn', models.CharField(blank=True, db_column='SECURE_KEY_SN', max_length=20, null=True)),
                ('user_priv', models.IntegerField(blank=True, db_column='USER_PRIV', null=True)),
                ('user_priv_no', models.IntegerField(blank=True, db_column='USER_PRIV_NO', null=True)),
                ('user_priv_name', models.CharField(blank=True, db_column='USER_PRIV_NAME', max_length=40, null=True)),
                ('post_priv', models.CharField(blank=True, db_column='POST_PRIV', max_length=1, null=True)),
                ('post_dept', models.TextField(blank=True, db_column='POST_DEPT', null=True)),
                ('dept_id', models.IntegerField(blank=True, db_column='DEPT_ID', null=True)),
                ('dept_id_other', models.CharField(blank=True, db_column='DEPT_ID_OTHER', max_length=100, null=True)),
                ('view_dept_id', models.CharField(blank=True, db_column='VIEW_DEPT_ID', max_length=100, null=True)),
                ('view_uid', models.CharField(blank=True, db_column='VIEW_UID', max_length=100, null=True)),
                ('view_priv_id', models.CharField(blank=True, db_column='VIEW_PRIV_ID', max_length=100, null=True)),
                ('leave_dept', models.IntegerField(blank=True, db_column='LEAVE_DEPT', null=True)),
                ('sex', models.CharField(blank=True, db_column='SEX', max_length=1, null=True)),
                ('birthday', models.DateTimeField(blank=True, db_column='BIRTHDAY', null=True)),
                ('is_lunar', models.CharField(blank=True, db_column='IS_LUNAR', max_length=1, null=True)),
                ('tel_no_dept', models.CharField(blank=True, db_column='TEL_NO_DEPT', max_length=50, null=True)),
                ('fax_no_dept', models.CharField(blank=True, db_column='FAX_NO_DEPT', max_length=50, null=True)),
                ('add_home', models.CharField(blank=True, db_column='ADD_HOME', max_length=200, null=True)),
                ('post_no_home', models.CharField(blank=True, db_column='POST_NO_HOME', max_length=50, null=True)),
                ('tel_no_home', models.CharField(blank=True, db_column='TEL_NO_HOME', max_length=50, null=True)),
                ('mobil_no', models.CharField(blank=True, db_column='MOBIL_NO', max_length=50, null=True)),
                ('bp_no', models.CharField(blank=True, db_column='BP_NO', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=50, null=True)),
                ('oicq_no', models.CharField(blank=True, db_column='OICQ_NO', max_length=50, null=True)),
                ('icq_no', models.CharField(blank=True, db_column='ICQ_NO', max_length=50, null=True)),
                ('msn', models.CharField(blank=True, db_column='MSN', max_length=200, null=True)),
                ('avatar', models.CharField(blank=True, db_column='AVATAR', max_length=20, null=True)),
                ('call_sound', models.IntegerField(blank=True, db_column='CALL_SOUND', null=True)),
                ('last_visit_time', models.DateTimeField(blank=True, db_column='LAST_VISIT_TIME', null=True)),
                ('sms_on', models.CharField(blank=True, db_column='SMS_ON', max_length=1, null=True)),
                ('menu_type', models.CharField(blank=True, db_column='MENU_TYPE', max_length=1, null=True)),
                ('last_pass_time', models.DateTimeField(blank=True, db_column='LAST_PASS_TIME', null=True)),
                ('theme', models.IntegerField(blank=True, db_column='THEME', null=True)),
                ('shortcut', models.TextField(blank=True, db_column='SHORTCUT', null=True)),
                ('portal', models.CharField(blank=True, db_column='PORTAL', max_length=20, null=True)),
                ('panel', models.CharField(blank=True, db_column='PANEL', max_length=1, null=True)),
                ('online', models.IntegerField(blank=True, db_column='ONLINE', null=True)),
                ('on_status', models.CharField(blank=True, db_column='ON_STATUS', max_length=1, null=True)),
                ('attend_status', models.CharField(blank=True, db_column='ATTEND_STATUS', max_length=1, null=True)),
                ('mobil_no_hidden', models.CharField(blank=True, db_column='MOBIL_NO_HIDDEN', max_length=1, null=True)),
                ('mytable_left', models.CharField(blank=True, db_column='MYTABLE_LEFT', max_length=200, null=True)),
                ('mytable_right', models.CharField(blank=True, db_column='MYTABLE_RIGHT', max_length=200, null=True)),
                ('user_priv_other', models.CharField(blank=True, db_column='USER_PRIV_OTHER', max_length=100, null=True)),
                ('user_no', models.IntegerField(blank=True, db_column='USER_NO', null=True)),
                ('not_login', models.IntegerField(blank=True, db_column='NOT_LOGIN', null=True)),
                ('not_view_user', models.CharField(blank=True, db_column='NOT_VIEW_USER', max_length=1, null=True)),
                ('not_view_table', models.CharField(blank=True, db_column='NOT_VIEW_TABLE', max_length=1, null=True)),
                ('not_search', models.CharField(blank=True, db_column='NOT_SEARCH', max_length=1, null=True)),
                ('bkground', models.CharField(blank=True, db_column='BKGROUND', max_length=200, null=True)),
                ('bind_ip', models.CharField(blank=True, db_column='BIND_IP', max_length=200, null=True)),
                ('last_visit_ip', models.CharField(blank=True, db_column='LAST_VISIT_IP', max_length=20, null=True)),
                ('menu_image', models.CharField(blank=True, db_column='MENU_IMAGE', max_length=10, null=True)),
                ('weather_city', models.CharField(blank=True, db_column='WEATHER_CITY', max_length=50, null=True)),
                ('show_rss', models.CharField(blank=True, db_column='SHOW_RSS', max_length=1, null=True)),
                ('my_rss', models.TextField(blank=True, db_column='MY_RSS', null=True)),
                ('remark', models.TextField(blank=True, db_column='REMARK', null=True)),
                ('menu_expand', models.CharField(blank=True, db_column='MENU_EXPAND', max_length=4, null=True)),
                ('my_status', models.CharField(blank=True, db_column='MY_STATUS', max_length=200, null=True)),
                ('limit_login', models.CharField(blank=True, db_column='LIMIT_LOGIN', max_length=1, null=True)),
                ('photo', models.CharField(blank=True, db_column='PHOTO', max_length=20, null=True)),
                ('im_range', models.IntegerField(blank=True, db_column='IM_RANGE', null=True)),
                ('leave_time', models.DateTimeField(blank=True, db_column='LEAVE_TIME', null=True)),
                ('secret_level', models.IntegerField(blank=True, db_column='SECRET_LEVEL', null=True)),
                ('user_para', models.TextField(blank=True, db_column='USER_PARA', null=True)),
                ('not_mobile_login', models.IntegerField(blank=True, db_column='NOT_MOBILE_LOGIN', null=True)),
                ('manage_module_type', models.CharField(blank=True, db_column='MANAGE_MODULE_TYPE', max_length=50, null=True)),
                ('user_priv_type', models.IntegerField(blank=True, db_column='USER_PRIV_TYPE', null=True)),
                ('user_manage_orgs', models.CharField(blank=True, db_column='USER_MANAGE_ORGS', max_length=200, null=True)),
                ('device_number', models.CharField(blank=True, db_column='DEVICE_NUMBER', max_length=100, null=True)),
                ('mobil_no_bd', models.CharField(blank=True, db_column='MOBIL_NO_BD', max_length=20, null=True)),
                ('corp_id', models.CharField(blank=True, max_length=38, null=True)),
                ('theme_colour', models.CharField(blank=True, db_column='THEME_COLOUR', max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'OA用户',
                'verbose_name_plural': 'OA用户',
                'db_table': 'auto_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataset', models.CharField(db_column='dataset', default='其它数据库', max_length=100, verbose_name='数据集')),
                ('database', models.CharField(blank=True, db_column='database', max_length=100, null=True, verbose_name='数据库名称')),
                ('username', models.CharField(blank=True, db_column='username', max_length=100, null=True, verbose_name='用户名')),
                ('passwd', models.CharField(blank=True, db_column='passwd', max_length=100, null=True, verbose_name='密码')),
                ('ip', models.CharField(blank=True, db_column='ip', max_length=100, null=True, verbose_name='服务器地址')),
                ('inputdate', models.DateTimeField(blank=True, db_column='inputdate', default=datetime.datetime.now, null=True, verbose_name='录入时间')),
                ('remark', models.CharField(blank=True, db_column='remark', max_length=100, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '数据集信息',
                'verbose_name_plural': '数据集信息',
                'db_table': 'dataset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=20, verbose_name='所属部门')),
                ('depart_group', models.CharField(blank=True, max_length=20, null=True, verbose_name='部门小组')),
            ],
            options={
                'verbose_name': '部门信息',
                'verbose_name_plural': '部门信息',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '验证信息',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, db_column='Code', max_length=20, null=True, verbose_name='员工编码')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True, verbose_name='用户姓名')),
                ('identitynumber', models.CharField(blank=True, db_column='IdentityNumber', max_length=20, null=True, verbose_name='身份证')),
                ('deptid', models.IntegerField(blank=True, db_column='DeptID', null=True, verbose_name='部门ID')),
                ('jobrankid', models.IntegerField(blank=True, db_column='JobRankID', null=True, verbose_name='职级')),
                ('nationcode', models.CharField(blank=True, db_column='NationCode', max_length=10, null=True, verbose_name='籍贯')),
                ('birthday', models.DateTimeField(blank=True, db_column='Birthday', null=True, verbose_name='出生日期')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='手机号码')),
                ('qq', models.CharField(blank=True, max_length=50, null=True, verbose_name='QQ号码')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱地址')),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=1, null=True, verbose_name='性别')),
                ('hiredate', models.DateTimeField(blank=True, db_column='HireDate', null=True, verbose_name='入职日期')),
            ],
            options={
                'verbose_name': '人员信息',
                'verbose_name_plural': '人员信息',
                'db_table': 'emp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '用户信息',
                'managed': False,
            },
        ),
    ]
