from django.shortcuts import render, HttpResponse
import json


# Create your views here.


def load_views(request):
    return render(request, 'ajax1/01-load.html')


def server01(request):
    uname = request.POST['uname']
    uage = request.POST['uage']
    return render(request, 'ajax1/01-server.html', locals())


def get_views(request):
    return render(request, 'ajax1/02-get.html')


def server02(request):
    dic = {
        'uname': 'Uzumaki Natrto',
        'uage': 16
    }
    jsonStr = json.dumps(dic)
    return HttpResponse(jsonStr)


def post_views(request):
    return render(request, 'ajax1/03-post.html')


def server03(request):
    uname = request.POST['uname']
    uage = request.POST['uage']
    ugender = request.POST['ugender']
    return HttpResponse(uname + "  " + uage + "  " + ugender)


def ajax_views(request):
    return render(request, 'ajax1/04-ajax.html')


def server04(request):
    list1 = [
        {
            "cname": "Python",
            "teacher": "QTX"
        },
        {
            "cname": "WEB",
            "teacher": "ZHMM"
        }
    ]
    return HttpResponse(json.dumps(list1))
