from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def home(request):
	return HttpResponse("This is Home Page")


def about(request):
	return HttpResponse("This is About Page")


def contact(request):
	return HttpResponse("This is Contact Page")	


