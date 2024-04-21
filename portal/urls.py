from django.urls import path

from . import views

app_name = "portal"

urlpatterns = [
	path("student/<int:id>",views.student,name="student"),
	path("logout",views.logout_view,name="logout"),
]