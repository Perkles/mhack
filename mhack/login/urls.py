from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GithubRegistration, CreateProfile, Logout, ManualUserRegistration, Login

urlpatterns = [
    path('signup/', ManualUserRegistration.as_view()),
    path('signin/', Login.as_view()),
    path('signout/', Logout.as_view()),
    path('signin/github/callback', GithubRegistration.as_view()),
    path('profile/create', CreateProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)