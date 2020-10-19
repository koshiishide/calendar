from django import template 
import datetime


register = template.Library()

#0,1,2
@register.simple_tag
@register.filter 
def test2(day):
    tmp=day.weekday()
    if ((tmp==5)or(tmp==6)):
        return 1
    else:
        return 0


@register.simple_tag
@register.filter 
def test(a):
    dict = {1:0,2:0}
    list = a
    for k in list:
        try:
            if (int(k.type_name) >1):
                dict[1]+=1
                dict[2]+=1
            elif(int(k.type_name) == 1):
                dict[1]+=1
            else:
                continue
        except:
            continue
    if (((dict[1])>=2) and (dict[2]>=2)):
        return 0
    else:
        return 1