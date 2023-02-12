from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_users, name="get_all_users"),
    path("/<int:id>", views.update_user),
]
