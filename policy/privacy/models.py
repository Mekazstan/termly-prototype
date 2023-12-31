
from django.db import models

class PrivacyPolicyAnswer(models.Model):
    website = models.BooleanField(default=False,null=True, verbose_name="Website")
    mobile_application = models.BooleanField(default=False,null=True, verbose_name="Mobile application")
    facebook_application = models.BooleanField(default=False,null=True, verbose_name="Facebook application")

    def __str__(self):
        return "Privacy Policy Answers"

    class Meta:
        app_label = 'privacy'

class UrlAnswer(models.Model):
    website = models.URLField(blank=True, null=True, verbose_name="Website URL")
    mobile_application = models.URLField(blank=True, null=True, verbose_name="Mobile Application URL")
    facebook_application = models.URLField(blank=True, null=True, verbose_name="Facebook Application URL")

    def __str__(self):
        return "Privacy Policy URL"

    class Meta:
        app_label = 'privacy'

class EnglishSpellingOption(models.Model):
    name = models.CharField(blank=True,null=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'privacy'

class UserLocation(models.Model):
    US_users = models.CharField(blank=True, null=True,choices=[("Yes", "Yes"), ("No", "No")], verbose_name="Do you have users in the United States?", max_length=50)
    EU_users = models.CharField(blank=True, null=True,choices=[("Yes", "Yes"), ("No", "No")], verbose_name="Do you have users in the EU, UK, Switzerland, Iceland, Liechtenstein, or Norway?", max_length=50)
    Canada_users = models.CharField(blank=True, null=True, choices=[("Yes", "Yes"), ("No", "No")], verbose_name="Do you have users in Canada?", max_length=50)
    
    def __str__(self):
        return "User Location Answers"

    class Meta:
        app_label = 'privacy'

class RegistrationOption(models.Model):
    option = models.CharField(default="No", null=True, max_length=3, choices=[("Yes", "Yes"), ("No", "No")])

    def __str__(self):
        return self.option

    class Meta:
        app_label = 'privacy'

class UserAge(models.Model):
    choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    target_users_under_18 = models.CharField(
        max_length=3,
        choices=choices,
        default="No",
        null=True
    )

    def __str__(self):
        return f'Target Users Under 18: {self.target_users_under_18}'

    class Meta:
        app_label = 'privacy'

class PersonalInfoOption(models.Model):
    name = models.CharField(null=True,blank=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'privacy'

class SelectedInfo(models.Model):
    selected_options = models.ManyToManyField(PersonalInfoOption, blank=True)

    class Meta:
        app_label = 'privacy'

class SensitiveInfo(models.Model):
    option = models.CharField(default="No", null=True, max_length=3, choices=[("Yes", "Yes"), ("No", "No")])

    def __str__(self):
        return self.option

    class Meta:
        app_label = 'privacy'

class SocialReg(models.Model):
    option = models.CharField(default="No", null=True, max_length=3, choices=[("Yes", "Yes"), ("No", "No")])

    def __str__(self):
        return self.option

    class Meta:
        app_label = 'privacy'

class DerivData(models.Model):
    option = models.CharField(default="No", null=True, max_length=3, choices=[("Yes", "Yes"), ("No", "No")])

    def __str__(self):
        return self.option

    class Meta:
        app_label = 'privacy'

class InfoApp(models.Model):
    choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    user_will_request_geolocation = models.CharField(null=True, choices=choices,
        blank=True, max_length=50,
        verbose_name="Will you be requesting access to your users' geolocations?"
    )
    user_will_request_features = models.CharField(null=True, choices=choices,
        blank=True, max_length=50,
        verbose_name="Will you be requesting access to features on your users' mobile devices?"
    )
    user_will_collect_device_info = models.CharField(null=True, choices=choices,
        blank=True, max_length=50,
        verbose_name="Will you be collecting any information regarding your users' mobile devices?"
    )
    user_will_send_push_notifications = models.CharField(null=True, choices=choices,
        blank=True, max_length=50,
        verbose_name="Will you be sending push notifications to your users?"
    )
    has_offer_wall = models.CharField(null=True, choices=choices,
        blank=True, max_length=50,
        verbose_name="Does your mobile app have an 'offer wall'?"
    )

    class Meta:
        app_label = 'privacy'