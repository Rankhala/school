from django.urls import path

from . import views

app_name = "front"

urlpatterns = [
	path("",views.index,name="index"),
	path("events",views.events,name="events"),
	path("login",views.login_view,name="login"),
	path("about",views.about,name="about"),
	path("term_results",views.term_results,name="term_results")

]