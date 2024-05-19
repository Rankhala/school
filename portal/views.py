from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from front.models import User, Grade, Subject, Student, Mark, Announcement
from .models import *

# Create your views here.
def student(request,id):
    student_data = User.objects.get(pk=id)
    all_announcements = Announcement.objects.all().order_by("id").reverse()
    marks = Mark.objects.filter(student=request.user.id)
    return render(request, "portal/student.html", {
            "student_data": student_data,
            "all_announcements": all_announcements,
            "marks": marks,
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("front:index"))