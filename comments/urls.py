from django.urls import path
from .views import CommentsView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', CommentsView.as_view(), name='comments'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/change', CommentUpdateView.as_view(), name='update_comment'),
    path('<int:pk>/delete', CommentDeleteView.as_view(), name='delete_comment'),
]
