from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import myuser, students, Track
from .forms import studForm, studForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
# Create your views here.
def registeruser(req):
    context = {}
    if(req.method=='GET'):
        return  render(req,'register.html')
    else:
        print(req.POST)
        myuser.objects.create(name=req.POST['username'],password=req.POST['password'])
        user=myuser.objects.all()

        return redirect('/login',{'users':user})

'''def login(request):
    context={}
    if(request.method=='GET'):
        context['users']=myuser.objects.all()
        return render(request, 'login.html',context)
    else:
        #check for user and passs
        username=request.POST['username']
        password=request.POST['password']
        #if correct
        user= myuser.objects.filter(name=username,password=password)
        if(len(user)>0):
            user=user[0]
        if(user):
            #go to home page
            return redirect('/home')

        else:
            #else print errr statment
            context['errormsg']='Invalid credentials.'
            return render(request, 'login.html', context)'''

def home(request):
    return render(request,'home.html')

def addstud(request):
    if (request.method == 'GET'):
        return render(request, 'addstud.html')
    else:
        print(request.POST)
        students.objects.create(name=request.POST['name'], track=request.POST['track'])
        stud = students.objects.all()

        return redirect('/add', {'student': stud})
def update(request):
    if (request.method == 'GET'):
        return render(request, 'update.html')
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        track = request.POST.get('track')

        students.objects.filter(id=id).update(name=name, track=track)
        return render(request, 'update.html')
def delete(request):
    if (request.method == 'GET'):
        return render(request, 'delete.html')
    else:
        id = request.POST['id']

        students.objects.filter(id=id).delete()
        return render(request, 'delete.html')

def selectall(request):
    context = {}
    context['studs'] = students.objects.all()
    return render(request, 'select.html', context)

def search(request):
    if (request.method == 'GET'):
        return render(request, 'search.html')
    else:
        name = request.POST['name']
        context = {}
        context['studs'] = students.objects.filter(name__icontains=name)
        return render(request, 'search.html', context)

#////////////////////////////////// Day 3 ////////////////////////
def mylogout(request):
    request.session['username']=None
    logout(request)
    return render(request, 'login.html')

def loginuserandadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        authuser = authenticate(username=username,password=password)
        userr=myuser.objects.filter(name=username,password=password)

        if(authuser is not None and userr is not  None):
            request.session['username']=username
            login(request, authuser)
            return render(request,'home.html',context)
        else:
            context['msg'] = 'Invalid credentials'
            return render(request, 'login.html', context)
def addusertoadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request,'addusertoadmin.html',context)
    else:
        usernmae=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        myuser.objects.create(name=usernmae,password=password)
        User.objects.create_user(username=usernmae,email=email,password=password,is_staff="True")
        return render(request, 'login.html', context)

class TrackList(ListView):
    model=Track

def insertstud(request):
    context = {}
    form = studForm()
    if (request.method == 'GET'):
        context['form'] = form
        return render(request, 'insertstud.html', context)
    else:
        students.objects.create(name=request.POST['name'], track=request.POST['track'])
        return render(request, 'home.html', context)


def insertstudusingModelForm(request):
    context={}
    form=studForm2()
    if(request.method=='GET'):
        context['form']=form
        return render(request,'insertstud.html',context)
    else:
        students.objects.create(name=request.POST['name'], track=request.POST['track'])
        return render(request, 'home.html', context)

