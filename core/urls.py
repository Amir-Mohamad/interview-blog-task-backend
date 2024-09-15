from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article-list'), 
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'), 
]
