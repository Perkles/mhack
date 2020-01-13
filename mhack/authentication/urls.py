from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication import views

urlpatterns = [
    path('signup/', views.ManualUserRegistration.as_view()),
    path('signin/github/callback', views.GithubRegistration.as_view()),
    path('signout/', views.Logout.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)