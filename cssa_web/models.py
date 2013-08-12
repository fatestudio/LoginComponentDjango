from django.db import models
from django.contrib.auth.models import User 
from django import forms

char_max_len = 50

# Create your models here.
class UserBase(models.Model):
    STUDENT_STATUS = (
        (u'U', u'Undergraduate'),
        (u'G', u'Graduate'),
    )
    account_name = models.CharField(max_length=char_max_len)
    account_password = models.CharField(max_length=char_max_len)
    
    first_name = models.CharField(max_length=char_max_len)
    last_name = models.CharField(max_length=char_max_len)
    major = models.CharField(max_length=char_max_len)
    student_status = models.CharField(max_length=char_max_len, choices=STUDENT_STATUS) 
    ucsb_email = models.EmailField()
    
    gmail_account = models.CharField(max_length=char_max_len)
    qq_account = models.CharField(max_length=char_max_len)
    renren_account = models.CharField(max_length=char_max_len)
    facebook_account = models.CharField(max_length=char_max_len)
    
    profile_photo = models.ImageField(upload_to='prof_photos')
    
    class Meta:
        abstract = True
        ordering = ['last_name']
        
class User(User):
    ucsb_email = models.EmailField()
    is_confirmed = models.BooleanField(default=False)
    is_newstudent = models.BooleanField(default=False)
    arrival_time = models.DateTimeField(null=True, blank=True)
    arrival_method = models.CharField(max_length=char_max_len, null=True, blank=True)
    def __unicode__(self):
        return self.username

class UserForm(forms.ModelForm):
    confirm_pwd = forms.CharField( widget=forms.PasswordInput, label="Confirm Password" )
    
    class Meta:
        model = User
        fields = ('username', 'ucsb_email', 'password', 'confirm_pwd')
        widgets = {
            'password': forms.PasswordInput,
        }
    def clean_ucsb_email(self):
        u_email = self.cleaned_data['ucsb_email']
        if("ucsb.edu" not in str(u_email)):
            self._errors["ucsb_email"] = self.error_class(["Please provide an UCSB email!"])
        if(User.objects.filter(ucsb_email=str(u_email))):   #must use filter! exist and get is not good!
            self._errors["ucsb_email"] = self.error_class(["This ucsb_email has been occupied!"])
        return u_email
    def clean_confirm_pwd(self):
        print(self.cleaned_data)
        password = self.cleaned_data['password']
        confirm_pwd = self.cleaned_data['confirm_pwd']

        if(str(password) != str(confirm_pwd)):   #must use filter! exist and get is not good!
            self._errors["confirm_pwd"] = self.error_class(["password and confirm password are different!"])
        return password
    
class UserConfirm(models.Model):
    user = models.ForeignKey(User)
    checknum = models.CharField(max_length=char_max_len)
#
#class UserLoginForm(forms.Form):
#    username = forms.CharField(max_length=char_max_len)
#    password = forms.PasswordInput()

class Album(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=char_max_len)
    
class Photo(models.Model):
    creator = models.ForeignKey(User)
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=char_max_len)
    img = models.ImageField(upload_to='photos')
    
class Event(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=char_max_len)
    album = models.ManyToManyField(Album)
    description = models.CharField(max_length=50000)
    begin_date = models.TimeField()
    end_date = models.TimeField()
    pub_date = models.TimeField()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'begin_date', 'end_date')
        widgets = {
            'description': forms.Textarea,
            'begin_date': forms.TimeInput,
            'end_date': forms.DateTimeInput,
        }
 
class File(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=char_max_len)
    description = models.CharField(max_length=50000, null=True, blank=True)
    _file = models.FileField(upload_to='files')
    pub_date = models.TimeField()

class ResourceForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'description', '_file')
        widgets = {
            'description': forms.Textarea,
        }        
