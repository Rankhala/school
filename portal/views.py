from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from front.models import User
from .models import *

# Create your views here.
def student(request,id):
    student_data = User.objects.get(pk=id)
    return render(request, "portal/student.html", {
            "student_data": student_data
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("front:index"))