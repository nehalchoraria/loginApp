from django.shortcuts import render
from django.http import HttpResponse
import random,string,json

def login(request):
    # CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
    # print(CLIENT_ID)
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    context = {'state':state}
    return render(request,'auth/index.html', context )

def home(request):
    return render(request,'home.html')
