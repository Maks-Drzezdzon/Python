from django.urls import path

from . import views

urlpatterns = [
	# page mapping, code mapping, name of mapping
    path("", views.index, name="index"),
    path("view1/", views.view1, name="test 1")
]