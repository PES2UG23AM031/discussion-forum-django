from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import QuestionForm, RegisterForm, ReplyForm, TopicForm
from .models import Question, Reply, Topic


def home(request):
    topics = Topic.objects.annotate(post_count=Count("questions")).order_by("name")
    latest_questions = Question.objects.select_related("topic", "author")[:5]
    return render(
        request,
        "forum_app/home.html",
        {"topics": topics, "latest_questions": latest_questions},
    )


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome to the forum!")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def create_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            messages.success(request, "Topic created successfully.")
            return redirect(topic)
    else:
        form = TopicForm()

    return render(request, "forum_app/question_form.html", {"form": form, "title": "Create Topic"})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    questions = topic.questions.select_related("author").annotate(reply_count=Count("replies"))
    return render(
        request,
        "forum_app/topic_detail.html",
        {"topic": topic, "questions": questions},
    )


@login_required
def create_question(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.topic = topic
            question.author = request.user
            question.save()
            messages.success(request, "Question posted successfully.")
            return redirect(question)
    else:
        form = QuestionForm()

    return render(
        request,
        "forum_app/question_form.html",
        {"form": form, "title": f"Ask a Question in {topic.name}"},
    )


def question_detail(request, pk):
    question = get_object_or_404(
        Question.objects.select_related("topic", "author"),
        pk=pk,
    )
    replies = question.replies.select_related("author")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please login to reply.")
            return redirect("login")

        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.question = question
            reply.author = request.user
            reply.save()
            messages.success(request, "Reply added successfully.")
            return redirect(question)
    else:
        reply_form = ReplyForm()

    return render(
        request,
        "forum_app/question_detail.html",
        {"question": question, "replies": replies, "reply_form": reply_form},
    )


@login_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.author != request.user:
        messages.error(request, "You can edit only your own questions.")
        return redirect(question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "Question updated successfully.")
            return redirect(question)
    else:
        form = QuestionForm(instance=question)

    return render(request, "forum_app/question_form.html", {"form": form, "title": "Edit Question"})


@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.author != request.user:
        messages.error(request, "You can delete only your own questions.")
        return redirect(question)

    topic = question.topic
    if request.method == "POST":
        question.delete()
        messages.success(request, "Question deleted successfully.")
        return redirect(topic)

    return render(
        request,
        "forum_app/confirm_delete.html",
        {"object": question, "cancel_url": question.get_absolute_url()},
    )


@login_required
def edit_reply(request, pk):
    reply = get_object_or_404(Reply.objects.select_related("question"), pk=pk)
    if reply.author != request.user:
        messages.error(request, "You can edit only your own replies.")
        return redirect(reply.question)

    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, "Reply updated successfully.")
            return redirect(reply.question)
    else:
        form = ReplyForm(instance=reply)

    return render(request, "forum_app/reply_form.html", {"form": form, "reply": reply})


@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(Reply.objects.select_related("question"), pk=pk)
    if reply.author != request.user:
        messages.error(request, "You can delete only your own replies.")
        return redirect(reply.question)

    question = reply.question
    if request.method == "POST":
        reply.delete()
        messages.success(request, "Reply deleted successfully.")
        return redirect(question)

    return render(
        request,
        "forum_app/confirm_delete.html",
        {"object": reply, "cancel_url": question.get_absolute_url()},
    )


def search_questions(request):
    query = request.GET.get("q", "").strip()
    results = Question.objects.none()
    if query:
        results = (
            Question.objects.select_related("topic", "author")
            .filter(Q(title__icontains=query) | Q(description__icontains=query))
            .annotate(reply_count=Count("replies"))
        )

    template = "forum_app/search_results.html"
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        template = "forum_app/includes/question_results.html"

    return render(request, template, {"query": query, "results": results})


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    questions = profile_user.questions.select_related("topic")
    context = {
        "profile_user": profile_user,
        "questions": questions,
        "total_questions": questions.count(),
        "total_replies": profile_user.replies.count(),
    }
    return render(request, "forum_app/profile.html", context)

