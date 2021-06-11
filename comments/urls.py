from django.urls import path
from .views import CommentList, CommentDetail, CommentsByAuthor

urlpatterns = [
    path('', CommentList.as_view()),
    path('detail/<int:pk>/', CommentDetail.as_view()),
    path('by_author/<int:author_id>/', CommentsByAuthor.as_view())

]
