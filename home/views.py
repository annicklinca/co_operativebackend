from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import HttpResponse, JsonResponse
import requests
from .serializers import *
import hashlib
import random

# Create your views here.

@csrf_exempt
def home(request):
    return HttpResponse('<center><font color="blue"><h1>Welcome to Co_operative</h1></font></center>')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken !')
                return redirect('register') 
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created !')
                return redirect('login')
                
        else:
            messages.info(request,'Password not match.. !')
            return redirect('register')
        return redirect('/')

    # else:
    #     return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signing')
    # else:
    #     return render(request, 'signin.html')

@csrf_exempt
def Production(request):
   
    if request.method == 'GET':
        reg = Production.objects.all()
        serializer = ProductionSerializer()(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = ProductionSerializer()(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  

@csrf_exempt
def ProductSerializer(request):
   
    if request.method == 'GET':
        reg = Product.objects.all()
        serializer = ProductSerializer()(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = ProductSerializer()(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  
