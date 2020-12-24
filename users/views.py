from django.shortcuts import render, HttpResponse
from . import models
import json
from django.core import serializers


# Create your views here.


def userindex(request):
    return render(request, 'users/user.html')


def chkUname(request):
    name = request.GET['uname']
    users = models.User.objects.filter(uname=name).all()
    if users:
        return HttpResponse("1")
    else:
        return HttpResponse("0")


def reguser(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    nickname = request.POST['nickname']
    try:
        models.User.objects.create(uname=uname, upwd=upwd, nickname=nickname)
        return HttpResponse("success")
    except:
        return HttpResponse("failed")


def query_user(request):
    return render(request, 'users/query.html')


def query_server(request):
    users = models.User.objects.all()
    msg = ''
    for u in users:
        msg += "%s_%s_%s_%s|" % (u.id, u.uname, u.upwd, u.nickname)
    msg = msg[0:-1]
    return HttpResponse(msg)


def json_views(request):
    return render(request, "users/json.html")


def json_server(request):
    dic = {
        'uname': "lase",
        'uage': 30,
        'ugender': 'male',
    }
    jsonstr = json.dumps(dic)
    str1 = serializers.serialize('json', models.User.objects.all())
    return HttpResponse(str1)


def user_server(request):
    users = models.User.objects.all()
    jsonstr = serializers.serialize('json', users)
    return HttpResponse(jsonstr)


def front_json(request):
    return render(request, 'users/front_json.html')


def front_server(request):
    jsonstr = request.GET['params']
    dic = json.loads(jsonstr)
    print(dic)
    return HttpResponse('success')