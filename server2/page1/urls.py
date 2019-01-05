from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/',views.home,name="home"), #Login page
    url('index/',views.index,name="index"),
    url('index2/',views.index2,name="index2"),
    url('index3/',views.index3,name="index3"),
    url('delete/(?P<name>[A-Z]*[a-z]+)',views.delete,name="delete"),
    url('update/(?P<name>[A-Z]*[a-z]+)/',views.update,name="update"),
    url('success_update/',views.success_update,name="success_update"),
    url('logins/',views.login_sites,name="login")
    #url('update/(?P<name>[A-Z]*[a-z]+)/(?P<salary>[0-9]+)',views.update,name="update")
]
