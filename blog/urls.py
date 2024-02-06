from django.urls import path
from .views import (
    blog_post_retrieve,
    blog_post_update,
    blog_post_delete,
    blog_post_list,
)

urlpatterns = [
    path('',                   blog_post_list),
    path('<str:slug>/',        blog_post_retrieve),
    path('<str:slug>/edit/',   blog_post_update),
    path('<str:slug>/delete/', blog_post_delete),
]
