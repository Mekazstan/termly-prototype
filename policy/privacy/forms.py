from django import forms
from .models import *

class PrivacyPolicyAnswerForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicyAnswer
        fields = ['website', 'mobile_application', 'facebook_application']

class UrlAnswerForm(forms.ModelForm):
    class Meta:
        model = UrlAnswer
        fields = ['website', 'mobile_application', 'facebook_application']

class EnglishSpellingOptionForm(forms.ModelForm):
    class Meta:
        model = EnglishSpellingOption
        fields = ['name']

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ['US_users', 'EU_users', 'Canada_users']

class RegistrationOptionForm(forms.ModelForm):
    class Meta:
        model = RegistrationOption
        fields = ['option']

class UserAgeForm(forms.ModelForm):
    class Meta:
        model = UserAge
        fields = ['target_users_under_18']

class PersonalInfoOptionForm(forms.ModelForm):
    class Meta:
        model = PersonalInfoOption
        fields = ['name']

class SelectedInfoForm(forms.ModelForm):
    class Meta:
        model = SelectedInfo
        fields = ['selected_options']

class SensitiveInfoForm(forms.ModelForm):
    class Meta:
        model = SensitiveInfo
        fields = ['option']

class SocialRegForm(forms.ModelForm):
    class Meta:
        model = SocialReg
        fields = ['option']

class DerivDataForm(forms.ModelForm):
    class Meta:
        model = DerivData
        fields = ['option']

class InfoAppForm(forms.ModelForm):
    class Meta:
        model = InfoApp
        fields = ['user_will_request_geolocation', 'user_will_request_features', 'user_will_collect_device_info', 'user_will_send_push_notifications', 'has_offer_wall']