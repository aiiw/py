from django.db import models

# Create your models here.
class Salary01(models.Model):
    choices = (('male', '男性'),('female', '女性'))
    周期 = models.TextField(blank=True, null=True)
    员工编号 = models.TextField(blank=True,choices = choices, null=True)
    平时加班时数 = models.FloatField(blank=True, null=True)
    周末加班时数 = models.FloatField(blank=True, null=True)
    节日加班时数 = models.FloatField(blank=True, null=True)
    有薪假时数 = models.FloatField(blank=True, null=True)
    法定假时数 = models.FloatField(blank=True, null=True)
    基本工资 = models.FloatField(blank=True, null=True)
    平均时薪 = models.FloatField(blank=True, null=True)
    法定日平均工资 = models.FloatField(blank=True, null=True)
    平时加班费 = models.FloatField(blank=True, null=True)
    公休日加班费 = models.FloatField(blank=True, null=True)
    节日加班费 = models.FloatField(blank=True, null=True)
    有薪假工资 = models.FloatField(blank=True, null=True)
    法定假工资 = models.FloatField(blank=True, null=True)
    最低工资补助 = models.FloatField(blank=True, null=True)
    计件工资 = models.FloatField(blank=True, null=True)
    全勤奖 = models.FloatField(blank=True, null=True)
    应发工资 = models.FloatField(blank=True, null=True)
    工龄奖 = models.FloatField(blank=True, null=True)
    公积金 = models.FloatField(blank=True, null=True)
    社保 = models.FloatField(blank=True, null=True)
    实发工资 = models.FloatField(blank=True, null=True)
    个税 = models.FloatField(blank=True, null=True)
    保健补助 = models.FloatField(blank=True, null=True)
    应税额 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary01'
        verbose_name = u'部门工资'
        verbose_name_plural = verbose_name