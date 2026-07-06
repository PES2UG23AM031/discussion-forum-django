from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("topics/new/", views.create_topic, name="create_topic"),
    path("topics/<int:pk>/", views.topic_detail, name="topic_detail"),
    path("topics/<int:topic_pk>/questions/new/", views.create_question, name="create_question"),
    path("questions/<int:pk>/", views.question_detail, name="question_detail"),
    path("questions/<int:pk>/edit/", views.edit_question, name="edit_question"),
    path("questions/<int:pk>/delete/", views.delete_question, name="delete_question"),
    path("replies/<int:pk>/edit/", views.edit_reply, name="edit_reply"),
    path("replies/<int:pk>/delete/", views.delete_reply, name="delete_reply"),
    path("search/", views.search_questions, name="search"),
    path("profiles/<str:username>/", views.profile, name="profile"),
]
