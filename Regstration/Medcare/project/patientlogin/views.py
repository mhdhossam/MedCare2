# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.contrib import messages
#
from .check import checkData
from.check import checkData1
from django.http import JsonResponse
from django.shortcuts import render
from .models import patientLogin,medicallogin


def json(request):
  password = patientLogin.getID()
  return JsonResponse(len(password),safe=False)

#homeuser
def homeuser(request):
  return render(request,'homelogin/Home.html')

#login for medicalproviders

def medlogin(request):
  if request.method=='POST':       
    email1=request.POST['email']
    password1=request.POST['password']
    
    email= medicallogin.getEmail()
    password = medicallogin.getPassword()
    checked =  checkData1(request,email,email1,password,password1)
    if checked :
      return redirect('/homeuser')
    else:
       messages.error(request,'kindly check your email and password :(')
      #   return render(request,'patientlogin/index.html',{'rs':password,'vs':email[i][0]})
    
  return render(request,'patientlogin/index.html') 

  
    

#login for patient
def login(request):
  if request.method=='POST':       
    email1=request.POST['email']
    password1=request.POST['password']
    
    email= patientLogin.getEmail()
    password = patientLogin.getPassword()
    checked =  checkData(request,email,email1,password,password1)
    if checked :
      return redirect('/homeuser')
    else:
       messages.error(request,'kindly check your email and password :(')
      #   return render(request,'patientlogin/index.html',{'rs':password,'vs':email[i][0]})
    
  return render(request,'patientlogin/index.html')

     
     #else:
         #return redirect(request,'patientlogin/index.html')



     
     
          # patiantdata = patientLogin.objects.all()
          
          # email= patiantdata.objects.values_list('email')
   #if pactientaccount.objects.filter(password=request.POST.get('password' ))== password1 and pactientaccount.objects.filter(email=request.POST.get('email' ))== email1 :
          # if email1==email1 and password1==password1 :
          #     return redirect('index.html')
          # else:
          #      messages.error(request,'error')
          #      return render(request,'patientlogin/index.html')
      #if pactientaccount.objects.filter(password=request.POST.get('password') ).exists()==password and pactientaccount.objects.filter(email=request.POST.get('email') ).exists()==email:  