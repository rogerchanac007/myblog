from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post_new/', views.post_new, name="post_new"),
    path('blog/<pk>', views.post_detail, name="post_detail"),
]