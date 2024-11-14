from django.db import models

class Question(models.Model):
    text = models.TextField()
    embeddings = models.FloatField()


class MarkScheme(models.Model):
    text = models.TextField()


class diagram(models.Model):
    explanation = models.TextField(null=True, blank=True)
    url = models.URLField()
    question = models.ForeignKey(Question, related_name="diagrams", on_delete=models.CASCADE, null=True, blank=True)
    mark_scheme = models.ForeignKey(MarkScheme, related_name="diagrams", on_delete=models.CASCADE, null=True, blank=True)