from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request, "front/index.html")

def events(request):
	return render(request, "front/events.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("portal:student",args=(request.user.id, )))        
        else:
            return render(request, "front/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "front/login.html")



