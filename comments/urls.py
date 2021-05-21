from django.urls import path, include
from rest_framework import routers
from .views import CommentsView, CommentDetailView
urlpatterns = [
    path('comments/', CommentsView.as_view(), name='comments'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail')
]