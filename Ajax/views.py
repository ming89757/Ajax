from django.shortcuts import HttpResponse, render


def xhr01(request):
    return render(request, '01-xhr.html')


def ajax_get(request):
    return render(request, '02-ajax-get.html')


def server02(request):
    return HttpResponse('this is use ajax.')


def server02_param(request):
    uname = request.GET.get('uname', '')
    return HttpResponse("Welcome: " + uname)


def ajax_post(request):
    return render(request, '03-ajax-post.html')


def server03(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse("username:%s,pwd: %s" % (uname, upwd))
