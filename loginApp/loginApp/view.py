from django.shortcuts import render
from django.http import HttpResponse

def loginPage(request):
    context = []
    return render(request,'auth/index.html', context )
