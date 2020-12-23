from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.


def userindex(request):
    return render(request, 'users/user.html')


def chkUname(request):
    name = request.GET['uname']
    users = models.User.objects.filter(uname=name).all()
    if users:
        return HttpResponse("user exist.")
    else:
        return HttpResponse("it is ok.")


def reguser(request):
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    nickname = request.GET['nickname']
    try:
        models.User.objects.create(uname=uname, upwd=upwd, nickname=nickname)
        return HttpResponse("success")
    except:
        return HttpResponse("failed")
