from django.urls import path, include
from rest_framework import routers
from .views import CommentsView, CommentDetailView, CommentCreateView

urlpatterns = [
    path('', CommentsView.as_view(), name='comments'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
]
