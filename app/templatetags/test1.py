from django import template 



register = template.Library()

#0,1,2
@register.simple_tag
def test2(a):
    return a


@register.simple_tag
@register.filter 
def test(a):
    dict = {1:0,2:0}
    list = a
    for k in list:
        if (int(k.type_name) >1):
            dict[1]+=1
            dict[2]+=1
        elif(int(k.type_name) == 1):
            dict[1]+=1
        else:
            continue
    if (((dict[1])>=2) and (dict[2]>=2)):
        return 0
    else:
        return 1