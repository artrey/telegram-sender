from django.http import HttpResponse


def send_view(request):
    print(request)
    return HttpResponse('Hello')
