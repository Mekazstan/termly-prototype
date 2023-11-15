from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe
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
      
    return render(request, './policy-uses/question1.html')

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

    return render(request, './policy-uses/question2.html')

def question3(request):
    if request.method == "POST":
        lang_name = request.POST.get("english_spelling")

        language = EnglishSpellingOption(
            name = lang_name
        )
        language.save()

    return render(request, './policy-uses/question3.html')

def question4(request):
    if request.method == "POST":
        location_input = request.POST.get("location")
        country_input = request.POST.get("country")
        canada_input = request.POST.get("canada")

        location = UserLocation(
            US_users =  location_input,
            EU_users =  country_input,
            Canada_users =  canada_input
        )
        location.save()

    return render(request, './user-info/question4.html')

def question5(request):
    if request.method == "POST":
        option = request.POST.get('create_register')

        option_url = RegistrationOption(
            option = option,
        )
        option_url.save()
    return render(request, './user-info/question5.html')

def question6(request):
    if request.method == "POST":
        user_age = request.POST.get('age')

        users_age = UserAge(
            target_users_under_18 = user_age,
        )
        users_age.save()
    return render(request, './user-info/question6.html')

def question7(request):
    # form1 = PersonalInfoOptionForm 
    # form2 = SelectedInfoForm
    return render(request, './collect-info/question7.html' ,)

def question8(request):
    if request.method == "POST":
        option = request.POST.get('sensitiveInfo')

        sensitive_info = SensitiveInfo(
            option = option,
        )
        sensitive_info.save()
    return render(request, './collect-info/question8.html')

def question9(request):
    if request.method == "POST":
        option = request.POST.get('socials')

        social_reg = SocialReg(
            option = option,
        )
        social_reg.save()
        
    return render(request, './collect-info/question9.html')


def question10(request):
    if request.method == "POST":
        option = request.POST.get('personalInfo')

        deriv_data = DerivData(
            option = option,
        )
        deriv_data.save()
    return render(request, './collect-info/question10.html')

def question11(request):
    if request.method == "POST":
        user_will_request_geolocation = request.POST.get('geolocations')
        user_will_request_features = request.POST.get('features')
        user_will_collect_device_info = request.POST.get('infomobile')
        user_will_send_push_notifications = request.POST.get('pushnotify')
        has_offer_wall = request.POST.get('offerwall')

        info_app = InfoApp(
            user_will_request_geolocation = user_will_request_geolocation,
            user_will_request_features = user_will_request_features,
            user_will_collect_device_info = user_will_collect_device_info,
            user_will_send_push_notifications = user_will_send_push_notifications,
            has_offer_wall = has_offer_wall
        )
        info_app.save()
    return render(request, './collect-info/question11.html')

def add_data(request):
    if request.method == 'POST':
        data = request.POST.get('data', '')
        # You can process or save the data as needed

        # Return a rendered HTML response with the updated content
        response_html = render_to_string('addform.html', {'data': data})
        return HttpResponse(response_html)

    return render(request, 'addform.html')
