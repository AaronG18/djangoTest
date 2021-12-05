from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def index(request):
    return render(request, 'index.html')


def indexView(request):
    c = ContentType.objects.values_list().all()
    print(c)
    return render(request, 'index.html')
