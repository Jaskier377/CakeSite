from django.urls import path
from .views import CommentList, CommentDetail, CommentsByAuthor, UserList, UserDetail

urlpatterns = [
    path('', CommentList.as_view()),
    path('detail/<int:pk>/', CommentDetail.as_view()),
    path('by_author/<int:author_id>/', CommentsByAuthor.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
