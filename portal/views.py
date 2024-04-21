from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def student(request,id):
	return render(request, "portal/student.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("front:login"))