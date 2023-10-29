from .models import priv_use, Apptype, lang_pref,userage,Userinfo,usersoc,derivdata,othersocial,Sensinfo,InfoDir
from django import forms

class priv_use_form(forms.ModelForm):
    class Meta:
        model = priv_use
        fields = ['selected_options']

class Apptype_form(forms.ModelForm):
    class Meta:
        model = Apptype
        fields = ['websitename','appname', 'faceappname']
        
class lang_pref_form(forms.ModelForm):
    class Meta:
        model = lang_pref
        fields = ['selected_option']

class userage_form(forms.ModelForm):
    class Meta:
        model = userage
        fields = ['selected_option']

class Userinfo_form(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['selected_option']

class usersoc_form(forms.ModelForm):
    class Meta:
        model = usersoc
        fields = ['selected_option']

class derivdata_form(forms.ModelForm):
    class Meta:
        model = derivdata
        fields = ['selected_option']

class othersocial_form(forms.ModelForm):
    class Meta:
        model = othersocial
        fields = ['selected_option']

class Sensinfo_form(forms.ModelForm):
    class Meta:
        model = Sensinfo
        fields = ['selected_option']

class Infodir_form(forms.ModelForm):
    class Meta:
        model = InfoDir
        fields = ['selected_options']
