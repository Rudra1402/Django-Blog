from django.urls import path, include
from post import views

urlpatterns = [
    path('', view=views.allBlogPosts, name="allblogs"),
    path('blog/<int:id>/', view=views.blogById, name="blog_detail"),
]
