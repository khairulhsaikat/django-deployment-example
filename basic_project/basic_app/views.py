from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from basic_app.models import AccessRecord,Topic,Webpage,User
from . import forms
from basic_app.forms import NewUserForm,UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records':webpages_list}
#     return render(request,'basic_app/index.html',context=date_dict)

def index(request):
    context_dict = {'text':'hello world','number':1000}
    return render(request,'basic_app/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{
                                    'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered':registered
                                })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active!")
        else:
            print('Someone tried to login and failed!!')
            print('Username {} and Password {}'.format(username,password))
            return HttpResponse("Invalid login details submitted!")
    else:
        return render(request,'basic_app/login.html',{})

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def other(request):
    return render(request,'basic_app/other.html')

def userpage(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR: FORM INVALID")

    return render(request,'basic_app/userpage.html',{'form':form})

def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request,'basic_app/form_page.html',{'form':form})
