from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial import views

urlpatterns = [
    path('tests/', views.Test_list.as_view()),
    path('test/<int:pk>/', views.Test_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)