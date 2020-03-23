from django.urls import path
from .views import *

urlpatterns = [
  path('ads/', AdListView.as_view()),
  path('ad/<str:pk>', AdDetailView.as_view()),
  path('comment/<str:pk>', CommentDetailView.as_view()),
  path('comments', CommentListView.as_view()),
  path('tag', TagCreateView.as_view()),
  path('tag/<str:pk>', TagDetailView.as_view())
]
