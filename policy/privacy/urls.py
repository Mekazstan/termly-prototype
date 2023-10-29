from django.urls import path,include
from . import views


urlpatterns = [
     path('', views.homeview, name='home'),
     path('privacy/', views.createview, name='createpolicy'),
     path('privacy/', views.Sensinfoview, name='sensitive'),
     path('privacy/', views.priv_useview, name='priv-pol-used'),
     path('privacy/', views.userinfoview, name='priv-pol-used'),
     path('privacy/', views.userageview, name='priv-pol-used'),
     path('privacy/', views.usersocview, name='priv-pol-used'),
     path('privacy/', views.derivdataview, name='priv-pol-used'),
     path('privacy/', views.othersocialview, name='priv-pol-used'),
     path('privacy/', views.infodirview, name='priv-pol-used'),
     path('privacy/', views.privacypolicy, name='priv-pol-used'),
     path('privacy/', views.Apptypeview, name='priv-pol-used'),
     


]
   