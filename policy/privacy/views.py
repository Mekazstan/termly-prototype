from django.shortcuts import render
from django.http import JsonResponse
from .models import (
    PrivacyPolicyAnswer, UrlAnswer, EnglishSpellingOption, UserLocation, RegistrationOption,
    UserAge, PersonalInfoOption, SelectedInfo, SensitiveInfo, SocialReg, DerivData,
    InfoApp
)

# from .forms import (
#     PrivacyPolicyAnswerForm, UrlAnswerForm, EnglishSpellingOptionForm, UserLocationForm, 
#     RegistrationOptionForm, UserAgeForm, PersonalInfoOptionForm, SelectedInfoForm, SensitiveInfoForm, 
#     SocialRegForm, DerivDataForm, InfoAppForm
# )

def homeview(request):
    
    return render(request, 'index.html' )

def createview(request):
    
    return render(request, 'popup.html' )


def dataview(request):
    page_mapping = {
    'question1': './policy-uses/question1.html',
    'question2': './policy-uses/question2.html',
    'question3': './policy-uses/question3.html',
    'question4': './user-info/question4.html',
    'question5': './user-info/question5.html',
    'question6': './user-info/question6.html',
    'question7': './collect-info/question7.html',
    'question8': './collect-info/question8.html',
    'question9': './collect-info/question9.html',
    'question10': './collect-info/question10.html',
    'question11': './collect-info/question11.html',
}
    # current_question = "question1"
   
    return render(request, 'base.html')
   
def privacypolicy(request):

    return render(request, "preview.html")

def question1(request):
    #  current_question = request.path
    if request.method == "POST":
        website = request.POST.get('website')
        mobile_application = request.POST.get('mobile_application')
        facebook_application = request.POST.get('facebook_application')

        privacy_answer = PrivacyPolicyAnswer(
            website=website,
            mobile_application=mobile_application,
            facebook_application=facebook_application
        )
        privacy_answer.save()
           
      
    return render(request, './policy-uses/question1.html' )

def question2(request):
    if request.method =="POST":
        website_url = request.POST.get('website_url')
        mobile_app_name = request.POST.get(' mobile_app_name')
        fb_app_name = request.POST.get('fb_app_name')

        privacy_url = UrlAnswer(
            website = website_url,
            mobile_application =  mobile_app_name,
            facebook_application = fb_app_name
        )
        privacy_url.save()

    return render(request, './policy-uses/question2.html' )

def question3(request):
    
    if request.method == "POST":
        lang_name = request.POST.get("english_spelling")

        language = EnglishSpellingOption(
            name = lang_name
        )
        language.save()
    return render(request, './policy-uses/question3.html')

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