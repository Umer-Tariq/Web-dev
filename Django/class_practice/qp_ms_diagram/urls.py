from django.urls import path, include
from .views import QuestionManager, MarkSchemeManager


urlpatterns = [
    path("question", QuestionManager.as_view(), name="question"),
    path("question/<int:id>", QuestionManager.as_view(), name="delete-question"),
    path("mark_scheme", MarkSchemeManager.as_view(), name="mark_scheme"),
]
