from django.contrib import admin

from .models import Question, Reply, Topic, UserProfile


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "author", "created_at")
    search_fields = ("title", "description", "author__username")
    list_filter = ("topic", "created_at")


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("question", "author", "created_at")
    search_fields = ("content", "author__username", "question__title")
    list_filter = ("created_at",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
