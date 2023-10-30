from django.shortcuts import render
from .models import (
    PrivacyPolicyAnswer, UrlAnswer, EnglishSpellingOption, UserLocation, RegistrationOption,
    UserAge, PersonalInfoOption, SelectedInfo, SensitiveInfo, SocialReg, DerivData,
    InfoApp
)

from .forms import (
    PrivacyPolicyAnswerForm, UrlAnswerForm, EnglishSpellingOptionForm, UserLocationForm, 
    RegistrationOptionForm, UserAgeForm, PersonalInfoOptionForm, SelectedInfoForm, SensitiveInfoForm, 
    SocialRegForm, DerivDataForm, InfoAppForm
)

def homeview(request):
    
    return render(request, 'index.html' )

def createview(request):
    
    return render(request, 'popup.html' )

def dataview(request):
    if request.method == "POST":
        form1 = PrivacyPolicyAnswerForm(request.POST)
        if form1.is_valid:
            form1.save()
        print(request.POST)
    return render(request, 'base.html' )

def privacypolicy(request):

    return render(request, "preview.html")

def question1(request):
    if request.method == "POST":
        form1 = PrivacyPolicyAnswerForm(request.POST)
        if form1.is_valid:
            form1.save()
        print(request.POST)
    return render(request, './policy-uses/question1.html' ,{"form1": form1} )

def question2(request):
    if request.method == "POST":
        form2 = UrlAnswerForm(request.POST)
        if form1.is_valid:
            form1.save()
        print(request.POST)
    
    return render(request, './policy-uses/question2.html' ,{"form2": form2} )

def question3(request):
    form = EnglishSpellingOptionForm
    return render(request, './policy-uses/question3.html' ,{"form": form} )

def question4(request):
    form = UserLocationForm
    return render(request, './user-info/question4.html' ,{"form": form} )

def question5(request):
    form = RegistrationOptionForm
    return render(request, './user-info/question5.html' ,{"form": form} )

def question6(request):
    form = UserAgeForm
    return render(request, './user-info/question6.html' ,{"form": form} )

def question7(request):
    form1 = PersonalInfoOptionForm 
    form2 = SelectedInfoForm
    return render(request, './collect-info/question7.html' ,{"form1": form1, "form2": form2} )

def question8(request):
    form = SensitiveInfoForm
    return render(request, './collect-info/question8.html' ,{"form": form} )

def question9(request):
    form = SocialRegForm
    return render(request, './collect-info/question9.html' ,{"form": form} )

def question10(request):
    form = DerivDataForm
    return render(request, './collect-info/question10.html' ,{"form": form} )

def question11(request):
    form = InfoAppForm
    return render(request, './collect-info/question11.html' ,{"form": form} )