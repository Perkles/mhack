from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userprofile import views

urlpatterns = [
    path('profile/create', views.CreateProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)