from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "front/index.html")

def about(request):
	pass

def login_view(request):
	pass

def logout_view(request):
	pass
