from django.urls import path

from . import views

urlpatterns = [
    path('<int:article_id>/', views.detail, name='detailed_article'),
    path('', views.get_all, name='articles'),
]
