from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import reverse
from django.urls import resolve
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.http import Http404


# Create your views here.
def mydate(request, year, month, day):
    # args = ['2019', '12', '12']
    # # reverse -> resolve
    # result = resolve(reverse('index:mydate', arg=args))
    # print('kwargs: ', result.kwargs)
    # print('url_name: ', result.url_name)
    # print('namespace: ', result.namespace)
    # print('view_name: ', result.view_name)
    # print('app_name: ', result.app_name)
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def index(request):
    # # return render(request, 'index.html')
    # kwargs = {'year': 2010, 'month': 2, 'day': 10}
    # args = ['2019', '12', '12']
    # # use reverse to generate address
    # print(reverse('index:mydate', args=args))
    # print(reverse('index:mydate', kwargs=kwargs))
    # return HttpResponse(reverse('index:mydate', args=args))
    # print(reverse('index:turnTo'))
    # return redirect(reverse('index:mydate', args=[2019, 12, 12]))
    # title = {'key': 'Hello MyDjango'}
    # content = {'key': 'This is MyDjango'}
    # return render(request, 'index.html', locals())
    # return redirect('index:shop', permanent=True)
    # set 302 redirect
    # url = reverse('index:shop')
    # return HttpResponseRedirect(url)
    # set 301 redirect
    # return HttpResponsePermanentRedirect(url)
    # Request.GET is to acquire request info
    if request.GET.get('error', ''):
        raise Http404('page does not exist')
    else:
        return render(request, 'index.html')


def shop(request):
    return render(request, 'index.html')


# def index(request, month):
#     value = 'This is test!'
#     print(value)
#     # return render(request, 'index.html')
#     return HttpResponse('this is variable outside urls scope: '+month)

#
# def indexView(request):
#     c = ContentType.objects.values_list().all()
#     print(c)
#     return render(request, 'index.html')


# def myvariable(request, year, month, day):
#     return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


# def mydate(request, year, month, day):
#     return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))
def pag_not_found(request, exception):
    # global 404 setting func
    return render(request, '404.html', status=404)


def page_error(request):
    # global 500 setting func
    return render(request, '500.html', status=500)
