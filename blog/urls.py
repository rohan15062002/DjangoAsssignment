from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.apiOverview, name="apiOverview"),
    path("posts/", views.blogListView, name="Posts"),
    path("posts/<int:id>/", views.blogDetailsView, name="Post Details"),
    path("create/", views.postCreate, name="Create"),
    path("detail/<int:id>/", views.postDetail, name="Detail"),
    path("update/<int:id>/", views.postUpdate, name="Update"),
    path("delete/<int:id>/", views.postDelete, name="Delete"),
]
