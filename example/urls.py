from django.urls import path
from . import views

app_name = "test_ajax_app"

urlpatterns = [
    path("", views.test_ajax_app),
    path("ajax/", views.test_ajax_response),
    path("ajax2/", views.test_ajax_response2),
]