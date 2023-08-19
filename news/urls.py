from django.urls import path

from .views import NewsCreateAndListAPIView, NewsDetailDestroyAPIView

urlpatterns = [
    path('api/news/', NewsCreateAndListAPIView.as_view(), name='news-create'),
    path('api/news/<int:pk>/', NewsDetailDestroyAPIView.as_view(), name='news-retrieve'),
]
