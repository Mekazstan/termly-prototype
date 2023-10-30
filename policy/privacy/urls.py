from django.urls import path,include
from . import views


urlpatterns = [
     path('', views.homeview, name='home'),
     path('privacy/create', views.createview, name='createpolicy'),
     path('privacy/data-input', views.dataview, name='data-input'),
     path('privacy/preview', views.privacypolicy, name='preview'),
     path('privacy/question1', views.question1, name='question1'),
     path('privacy/question2', views.question2, name='question2'),
     path('privacy/question3', views.question3, name='question3'),
     path('privacy/question4', views.question4, name='question4'),
     path('privacy/question5', views.question5, name='question5'),
     path('privacy/question6', views.question6, name='question6'),
     path('privacy/question7', views.question7, name='question7'),
     path('privacy/question8', views.question8, name='question8'),
     path('privacy/question9', views.question9, name='question9'),
     path('privacy/question10', views.question10, name='question10'),
     path('privacy/question11', views.question11, name='question11')
     ]