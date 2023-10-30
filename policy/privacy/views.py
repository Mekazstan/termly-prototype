from django.shortcuts import render
from .models import (
    PrivacyPolicyAnswer, UrlAnswer, EnglishSpellingOption, UserLocation, RegistrationOption,
    UserAge, PersonalInfoOption, SelectedInfo, SensitiveInfo, SocialReg, DerivData,
    UserGeolocation, UserMobileDevice, UserDeviceInfo, PushNotifications, OfferWall, OtherSources,
)

from .forms import (
    PrivacyPolicyAnswerForm, UrlAnswerForm, EnglishSpellingOptionForm, UserLocationForm, 
    RegistrationOptionForm, UserAgeForm, PersonalInfoOptionForm, SelectedInfoForm, SensitiveInfoForm, 
    SocialRegForm, DerivDataForm, UserGeolocationForm, UserMobileDeviceForm, UserDeviceInfoForm, 
    PushNotificationsForm, OfferWallForm, OtherSourcesForm,
)

def homeview(request):
    
    return render(request, 'index.html' )

def createview(request):
    
    return render(request, 'popup.html' )

def dataview(request):

    return render(request, 'base.html' )

def privacypolicy(request):

    return render(request, "preview.html")

def policy_useview(request):
    form = PrivacyPolicyAnswerForm
    return render(request, 'article-one.html' ,{"form": form} )