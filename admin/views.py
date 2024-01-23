from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render
from user.forms import UserRegistrationForm
from user.models import UserRegistrationModel, UserFirstImageModel, UserSecondImageModel
# Create your views here.

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admin/adminhome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'adminlogin.html', {})


def adminhome(request):
    return render(request,"admin/adminhome.html")

def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admin/viewregisterusers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admin/viewregisterusers.html',{'data':data})


def AdminResults(request):
    data = UserFirstImageModel.objects.all()
    data_ai = UserSecondImageModel.objects.all()
    from itertools import chain
    data = list(chain(data, data_ai))
    return render(request, 'admin/adminviewresults.html', {'data': data})