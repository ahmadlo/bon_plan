__author__ = 'AHMAD'
from django.conf.urls import url,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter(trailing_slash=False)
router.register(r'typesuser',views.TypeUserView)
urlpatterns = [

    url(r'/',include(router.urls)),

]
