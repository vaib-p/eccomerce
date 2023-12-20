from django.http import HttpResponse

def home(request):
    return HttpResponse('i amm at home')