from django import template 



register = template.Library()

#0,1,2

@register.simple_tag
def test(a):
    dict = {1:0,2:0}
    list = a
    for k in list:
        print(k)
        if (int(k.type_name) >1):
            dict[1]+=1
            dict[2]+=1
        elif(int(k.type_name) == 1):
            dict[1]+=1
        else:
            continue
    if (((dict[1])>=2) and (a[2]>=2)):
        return 1
    else:
        return 0