# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
        return render_to_response('login/index.html',)