from django.conf.urls import url
from django.urls import path
import youxian.views

urlpatterns = [
    # url(r"(?P<model>\w+)/(?P<object_id>\d+)/pay", youxian.views.pay_action),
    path('add_goods/', youxian.views.add_goods),
]
