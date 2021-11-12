import datetime

from django import template

register = template.Library()


#  若字符串长度大于30，则省略之后的内容，否则原样输出该字符串。参数value就是过滤器前的值
@register.filter
def truncate_chars(value):
    if value.__len__() > 30:
        return '%s......'% value[0:30]
    else:
        return value

# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('result.html')
def test():
    a=['first','second','third']
    return {'choices':a}