# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from medicalproviders.models import medicalproviders
from patientregister.models import pactientaccount 
def ai(request):
    return render(request,'model-ai/index.html')