from django.urls import path,include
from . import views


urlpatterns = [
     path('', views.homeview, name='home'),
     path('privacy/create', views.createview, name='createpolicy'),
     path('privacy/data-input', views.dataview, name='data-input'),
     path('privacy/preview', views.privacypolicy, name='preview'),
     path('privacy/policy-view', views.policy_useview, name='policy-view'),
     # path('privacy/', views.Sensinfoview, name='sensitive'),s
     
     # path('privacy/', views.userinfoview, name='priv-pol-used'),
     # path('privacy/', views.userageview, name='priv-pol-used'),
     # path('privacy/', views.usersocview, name='priv-pol-used'),ssss
     # path('privacy/', views.derivdataview, name='priv-pol-used'),
     # path('privacy/', views.othersocialview, name='priv-pol-used'),
     # path('privacy/', views.infodirview, name='priv-pol-used'),
     # path('privacy/', views.privacypolicy, name='priv-pol-used'),
     # path('privacy/', views.Apptypeview, name='priv-pol-used'),
     ]
   