from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from wgm_app_events import views

urlpatterns = [
    path('events/', views.EventsList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)