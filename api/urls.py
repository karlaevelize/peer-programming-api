from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # user paths
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # project paths
    path('projects/', views.ProjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
