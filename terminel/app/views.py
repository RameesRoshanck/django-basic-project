from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def home(request):
    if request.session.has_key('ses-id'):
        return render(request,'home.html')    
    else:
        return redirect('login')


def login(request):
    if request.session.has_key('ses-id'):
        return redirect('home') 
    else:
        if request.method=='POST':
            database={'username':'roshan','password':'123456'}
            username=request.POST['username']
            password=request.POST['password']
            print(username)
            if database['username']==username and database['password']==password:
                request.session['ses-id']='ses-id'
                print(username)
                return redirect('home')
            else:
                messages.info(request, 'incorrect username or password.')
                return redirect('home')
        else:
            return render(request,'login.html')


def logout(request):
    request.session.flush()
    return redirect('home')