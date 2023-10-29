from django.db import models

# Create your models here.

class priv_use(models.Model):
    selected = models.ManyToManyField(related_name="selected_answers", blank=True)
    
class Apptype(models.Model):
    selected_types = models.ManyToManyField(related_name="selected_answers", blank=True)
class lang_pref(models.Model):
    lang = models.ForeignKey(related_name="selected_answer", blank=True)

class Userinfo(models.Model):
    Usa_user = models.ForeignKey(related_name="selected_answer", blank=True)
    Eu_user = models.ForeignKey(related_name="selected_answer", blank=True)
    Can_user = models.ForeignKey(related_name="selected_answer", blank=True)

class Usercreate(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)
class userage(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)

class InfoDir(models.Model):
    selected = models.ManyToManyField(related_name="selected_answers", blank=True)

class Sensinfo(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)

class usersoc(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)

class derivdata(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)

class othersocial(models.Model):
    ans = models.ForeignKey(related_name="selected_answer", blank=True)

# class Useofinfo(models.Model):
#     Markprom = models.BooleanField(blank=True)
#     Onlinepay = models.BooleanField(blank=True)
#     Onlipost = models.BooleanField(blank=True)
   


# class Disclosure(models.Model):
#     Thirdparty = models.BooleanField(blank=True)
#     Busaff = models.BooleanField(blank=True)
#     Buspart = models.BooleanField(blank=True)
#     SecMea = models.BooleanField(blank=True)
   
# class Useoftra(models.Model):
#     Tracktech = models.BooleanField(blank=True)
#     cookiepol = models.BooleanField(blank=True)
#     googlemap = models.BooleanField(blank=True)
#     Cacheloc = models.BooleanField(blank=True)
    

# class Usconsid(models.Model):
#     statelaws = models.BooleanField(blank=True)


# class Euconsid(models.Model):
#     Eurep = models.BooleanField(blank=True)


# class Userrights(models.Model):
#     Dpo = models.BooleanField(blank=True)
#     datasub = models.BooleanField(blank=True)
#     UserReq = models.BooleanField(blank=True)
   
# class Final(models.Model):
#     ReviewPolicy = models.BooleanField(blank=True)
#     addclause = models.BooleanField(blank=True)
#     compName = models.CharField(blank=True)
#     shrtform = models.BooleanField(blank=True)
#     email = models.EmailField(blank=True)
#     phone = models.IntegerField(blank=True)
#     faxnum = models.IntegerField(blank=True)
#     country = models.CharField(blank=True)
#     address1 = models.CharField(blank=True)
#     address2 = models.CharField(blank=True)
#     City = models.CharField(blank=True)
#     postalcode = models.IntegerField(blank=True)
#     policyname = models.charfield(blank= True)
#     realdate = models.DateTimeField(blank=True)



