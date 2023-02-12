from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_users, name="get_all_users"),
    path("/new-user", views.create_user, name="create_user"),
    path("/<int:id>", views.update_user, name="update_user"),
]
