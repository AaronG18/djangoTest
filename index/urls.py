from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # path('', views.index, {'month': '2019/10/10'}),
    path('<year>/<int:month>/<slug:day>', views.mydate, name='mydate'),
    # # re_path denotes using regex to match urls
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate)

    # refine@page 57
    # re_path('(?P<year>[0-9]{4}).html', views.mydate, name='mydate'),
    path('', views.index, name='index'),
    path('TurnTo', RedirectView.as_view(url='/'), name='turnTo'),
    path('shop', views.shop, name='shop'),
]
