from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from cssa_web.models import User
from cssa_web.models import UserForm
from cssa_web.models import UserConfirm
from cssa_web.models import Event
from cssa_web.models import EventForm
from cssa_web.models import ResourceForm
from cssa_web.models import File
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from cssa_web.module.sendmail import sendConfirmEmail
from datetime import datetime
import os.path
def index(request):
    return render_to_response('cssa_web/pages/index.html')

def register(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserForm(request.POST) # A form bound to the POST data
        if(form.is_valid()):
            username = form.cleaned_data['username']
            ucsb_email = form.cleaned_data['ucsb_email']
            password = form.cleaned_data['password']
            user = User(username=username, ucsb_email=ucsb_email)
            user.set_password(password)
            user.save()
            sendConfirmEmail(user)
            return HttpResponseRedirect('/cssa/success/email_sent/') # Redirect after POST
        else:
            return HttpResponse(str(form.errors))

    else:
        form = UserForm() # An unbound form

    return render_to_response('cssa_web/pages/register.html', 
        {'form': form}, context_instance=RequestContext(request))   
    
def confirm(request, username, random_num):
    print(username, random_num)
    user = User.objects.filter(username=username)
    if(user.count() == 1):
        userconfirm = UserConfirm.objects.filter(user=user)
        if(userconfirm.count() == 1):
            if(userconfirm[0].checknum == random_num):
                usernew = user[0]
                usernew.is_confirmed = True
                user.delete()
                usernew.save()
                userconfirm.delete()
                return HttpResponse("Congratuations! You have confirmed!")
    return HttpResponse("Confirmation is not correct!")

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponse("Success!") # Redirect to a success page.
            else:
                return HttpResponse("disabled account")# Return a 'disabled account' error message
        else:
            return HttpResponse("invalid login")# Return an 'invalid login' error message.            
    else:
        return render_to_response('cssa_web/pages/login.html', context_instance=RequestContext(request)) # An unbound form

def logout_view(request):
    logout(request)
    return HttpResponse("Logout Success!") # Redirect to a success page.

def email_sent(request):
    return HttpResponse("An email has been sent to your UCSB email account. Please Confirm it.")
    
def event(request):
    event_list = Event.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('cssa_web/pages/event.html')
    c = Context({
        'event_list': event_list,
    })
    return HttpResponse(t.render(c))

def addEvent(request):
    if request.method == 'POST': # If the form has been submitted...
        print("in here")
        form = EventForm(request.POST, request.FILES) # A form bound to the POST data
        if(form.is_valid()):
            handle_uploaded_file(request.FILES['_file'])
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            _file = form.cleaned_data['_file']
            pub_date = datetime.now()
            user = User.objects.filter(username=request.user.username)
            print(request.user.username)
            print(user)
            resource = File(creator=user[0], name=name, description=description, _file=_file, pub_date=pub_date)
            resource.save()
            return HttpResponse('add Resource Success!') # Redirect after POST
        else:
            return HttpResponse(str(form.errors))
    else:
        if request.user.is_authenticated():
            form = EventForm() # An unbound form
            
            return render_to_response('cssa_web/pages/addResource.html', 
                {'form': form}, context_instance=RequestContext(request))   
        else:
            return HttpResponseRedirect('/cssa/login/')
    
def resource(request):
    file_list = File.objects.all().order_by('-pub_date')[:5]
    print(file_list)
    t = loader.get_template('cssa_web/pages/resource.html')
    c = Context({
        'resource_list': file_list,
    })
    return HttpResponse(t.render(c))

def handle_uploaded_file(f):
    with open('/home/fatestudio/workspacePython/cssa/cssa_web/files/' + f.name, 'wb+') as destination:
#        os.path.abspath(destination)
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()

def addResource(request):
    if request.method == 'POST': # If the form has been submitted...
        print("in here")
        form = ResourceForm(request.POST, request.FILES) # A form bound to the POST data
        if(form.is_valid()):
            handle_uploaded_file(request.FILES['_file'])
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            _file = form.cleaned_data['_file']
            pub_date = datetime.now()
            user = User.objects.filter(username=request.user.username)
            print(request.user.username)
            print(user)
            resource = File(creator=user[0], name=name, description=description, _file=_file, pub_date=pub_date)
            resource.save()
            return HttpResponse('add Resource Success!') # Redirect after POST
        else:
            return HttpResponse(str(form.errors))
    else:
        if request.user.is_authenticated():
            form = ResourceForm() # An unbound form
            
            return render_to_response('cssa_web/pages/addResource.html', 
                {'form': form}, context_instance=RequestContext(request))   
        else:
            return HttpResponseRedirect('/cssa/login/')
