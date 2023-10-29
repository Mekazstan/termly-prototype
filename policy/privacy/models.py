from django.db import models

# Create your models here.

class privacy(models.Model):
    priv_use = models.BooleanField(blank=True)
    Eng_pref = models.BooleanField(blank=True)
   
class Userinfo(models.Model):
    Usa_user = models.BooleanField(blank=True)
    Eu_user = models.BooleanField(blank=True)
    Can_user = models.BooleanField(blank=True)
    Usercreate = models.BooleanField(blank=True)
    Usertarget = models.BooleanField(blank=True)
   

class Collectinfo(models.Model):
    InfoDir = models.CharField(blank=True)
    SensInfo = models.BooleanField(blank=True)
    Userregsoc = models.BooleanField(blank=True)
    Derivdata = models.BooleanField(blank=True)
    OtherSoc = models.BooleanField(blank=True)
   

class Useofinfo(models.Model):
    Markprom = models.BooleanField(blank=True)
    Onlinepay = models.BooleanField(blank=True)
    Onlipost = models.BooleanField(blank=True)
   


class Disclosure(models.Model):
    Thirdparty = models.BooleanField(blank=True)
    Busaff = models.BooleanField(blank=True)
    Buspart = models.BooleanField(blank=True)
    SecMea = models.BooleanField(blank=True)
   
class Useoftra(models.Model):
    Tracktech = models.BooleanField(blank=True)
    cookiepol = models.BooleanField(blank=True)
    googlemap = models.BooleanField(blank=True)
    Cacheloc = models.BooleanField(blank=True)
    

class Usconsid(models.Model):
    statelaws = models.BooleanField(blank=True)


class Euconsid(models.Model):
    Eurep = models.BooleanField(blank=True)


class Userrights(models.Model):
    Dpo = models.BooleanField(blank=True)
    datasub = models.BooleanField(blank=True)
    UserReq = models.BooleanField(blank=True)
   
class Final(models.Model):
    ReviewPolicy = models.BooleanField(blank=True)
    addclause = models.BooleanField(blank=True)
    compName = models.CharField(blank=True)
    shrtform = models.BooleanField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=True)
    faxnum = models.IntegerField(blank=True)
    country = models.CharField(blank=True)
    address1 = models.CharField(blank=True)
    address2 = models.CharField(blank=True)
    City = models.CharField(blank=True)
    postalcode = models.IntegerField(blank=True)
    policyname = models.charfield(blank= True)
    realdate = models.DateTimeField(blank=True)



