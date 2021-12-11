from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse


# Create your views here.
def index(request, month):
    value = 'This is test!'
    print(value)
    # return render(request, 'index.html')
    return HttpResponse('this is variable outside urls scope: '+month)

#
# def indexView(request):
#     c = ContentType.objects.values_list().all()
#     print(c)
#     return render(request, 'index.html')


def myvariable(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def mydate(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))
