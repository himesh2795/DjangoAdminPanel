from django.urls import path,include
from . import views
urlpatterns = [
  path("",views.IndexPage,name="indexpage"),
  path("indexpage2/",views.IndexPage2,name="indexpage2"),
  path("registeruser/",views.registerUser,name="register"),
  path("showdetail/",views.ShowDetail,name="showdetail"),  
]
