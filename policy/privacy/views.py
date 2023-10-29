from django.shortcuts import render
from .forms import Sensinfo_form,priv_use_form, Apptype_form,Infodir_form,userage_form, usersoc_form, Userinfo_form,othersocial_form,lang_pref_form,derivdata_form
from .models import priv_use, Apptype, lang_pref,userage,Userinfo,usersoc,derivdata,othersocial,Sensinfo,InfoDir

def homeview(request):
    
    return render(request, '/' )

def createview(request):
    
    return render(request, '/templates/index.html' )

def Sensinfoview(request):
    form = Sensinfo_form
    return render(request, '/' ,{"form": form} )

def priv_useview(request):
    form = priv_use_form
    return render(request, './templates/policy-uses/article-one.html' ,{"form": form} )

def Apptypeview(request):
    form = Apptype_form
    return render(request, './templates/policy-uses/' ,{"form": form} )

def lang_prefview(request):
    form = lang_pref_form
    return render(request, './templates/policy-uses/article-website.html' ,{"form": form} )
    
def userageview(request):
    form = userage_form
    return render(request, '/' ,{"form": form} )

def userinfoview(request):
    form = Userinfo_form
    return render(request, '/' ,{"form": form} )

def usersocview(request):
    form = usersoc_form
    return render(request, "/", {"form": form})

def derivdataview(request):
    form = derivdata_form
    return render(request, "/", {"form": form})

def othersocialview(request):
    form = othersocial_form
    return render(request, "/", {"form": form})
def infodirview(request):
    form = Infodir_form
    return render(request, "/", {"form": form})



def privacypolicy(request):
    return render(request, "/")
