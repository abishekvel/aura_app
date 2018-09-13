from django.conf.urls import url,include
from iot import views

urlpatterns =[
    url(r'^', views.home,name='home'),

]
