from django.contrib import admin
from django.urls import path,include
from frontend import views
from .views import PostListView,PostDetailView,PostUpdateView
urlpatterns = [

    path('',PostListView.as_view(),name='home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='detail'),
     path('post/<int:pk>/update',PostUpdateView.as_view(),name='update'),
    path('editblog/',views.edit_blog,name='editblog'),
    path('portfolio/',views.portfolio,name='portfolio'),
]